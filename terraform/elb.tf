# Some aws resources must have account-wide unique names e.g. s3 buckets
# random_pet generates a random string that is recognizable

resource "random_pet" "this" {
  length = 2
}

##############################################################
# Data sources to get VPC, subnets and security group details
##############################################################

data "aws_subnet_ids" "all" {
  vpc_id = module.vpc.vpc_id
}

data "aws_security_group" "default" {
  vpc_id = module.vpc.vpc_id
  name   = "default"
}

#########################
# S3 bucket for ELB logs
#########################
data "aws_elb_service_account" "this" {}
# data source to get the Account ID of the AWS Elastic Load Balancing Service
# Account in a given region for the purpose of permitting in S3 bucket policy.

resource "aws_s3_bucket" "bizzabo_logs" {
  bucket        = "bizzabo-logs-${random_pet.this.id}"
  acl           = "private"
  policy        = data.aws_iam_policy_document.bizzabo_logs.json
  force_destroy = true
}

data "aws_iam_policy_document" "bizzabo_logs" {
  statement {
    actions = [
      "s3:PutObject",
    ]

    principals {
      type        = "AWS"
      identifiers = [data.aws_elb_service_account.this.arn]
    }

    resources = [
      "arn:aws:s3:::bizzabo-logs-${random_pet.this.id}/*",
    ]
  }
}

##################
# ACM certificate
##################
resource "aws_route53_zone" "bizzabo_demo" {
  name          = "bizzabo-demo.com"
  force_destroy = true
}

module "acm" {
  source  = "terraform-aws-modules/acm/aws"
  version = "~> 3.0"

  zone_id = aws_route53_zone.bizzabo_demo.zone_id

  domain_name               = "bizzabo-demo.com"
  subject_alternative_names = ["*.bizzabo-demo.com"]

  wait_for_validation = false
}

################
# Security Group
################

resource "aws_security_group" "allow_web" {
  name        = "allow_web"
  description = "Allow Web inbound traffic"
  vpc_id      = module.vpc.vpc_id

  ingress {
    description      = "HTTPS from Internet"
    from_port        = 443
    to_port          = 443
    protocol         = "tcp"
    cidr_blocks      = ["0.0.0.0/0"]
    ipv6_cidr_blocks = ["::/0"]
  }

  ingress {
    description      = "HTTP from Internet"
    from_port        = 80
    to_port          = 80
    protocol         = "tcp"
    cidr_blocks      = ["0.0.0.0/0"]
    ipv6_cidr_blocks = ["::/0"]
  }

  egress {
    from_port        = 0
    to_port          = 0
    protocol         = "-1"
    cidr_blocks      = ["0.0.0.0/0"]
    ipv6_cidr_blocks = ["::/0"]
  }

  tags = {
    Name = "allow_web"
  }
}

######
# ELB
######
module "elb" {
  source = "terraform-aws-modules/elb/aws"

  name = "bizzabo-elb"

  subnets         = module.vpc.public_subnets
  security_groups = [data.aws_security_group.default.id, aws_security_group.allow_web.id]
  internal        = false

  listener = [
    {
      instance_port     = "80"
      instance_protocol = "http"
      lb_port           = "80"
      lb_protocol       = "http"
    },
    {
      instance_port     = "443"
      instance_protocol = "http" # https (see below)
      lb_port           = "443"
      lb_protocol       = "http" # https (see below)

      # Note about SSL:

      # This line is commented out because ACM certificate has to be "Active" (validated and verified by AWS, but
      # Route53 zone used in this example is not real). To enable SSL in ELB: uncomment this line, then set 
      # "wait_for_validation = true" in ACM module and make sure that instance_protocol and lb_protocol are https or ssl.

      #ssl_certificate_id = module.acm.acm_certificate_arn
    },
  ]

  health_check = {
    target              = "HTTP:80/"
    interval            = 30
    healthy_threshold   = 2
    unhealthy_threshold = 2
    timeout             = 5
  }

  access_logs = {
    bucket = aws_s3_bucket.bizzabo_logs.id
  }

  tags = {
    Owner       = "yosef"
    Environment = "dev"
  }

  # ELB attachments
  number_of_instances = var.number_of_instances
  instances           = module.ec2_instances.id
}

################
# EC2 Images
################

data "aws_ami" "amazon-linux-2" {
  most_recent = true

  owners = ["amazon"]

  filter {
    name   = "name"
    values = ["amzn2-ami-hvm-*-x86_64-ebs"]
  }
}

################
# EC2 instances
################
module "ec2_instances" {
  source  = "terraform-aws-modules/ec2-instance/aws"
  version = "~> 2.0"

  instance_count = var.number_of_instances

  name                        = "bizzabo-app"
  ami                         = data.aws_ami.amazon-linux-2.id
  instance_type               = "t2.micro"
  vpc_security_group_ids      = [data.aws_security_group.default.id]
  subnet_id                   = element(tolist(data.aws_subnet_ids.all.ids), 0)
  associate_public_ip_address = true
}