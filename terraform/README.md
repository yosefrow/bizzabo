# Terraform Implementation

## AWS Infrastructure as Code 

Infrastructure as code for AWS was created using Terraform and includes the following

### VPC

- VPC with two public and private subnets (used 3 az according to best practices) (terraform/vpc.tf) (module.vpc.bizzabo-vpc)
- Route tables for each subnet (created automatically by the vpc module) (terraform/vpc.tf) (module.vpc.bizzabo-vpc)

### ELB

- Security Group to allow port 80 and 443 from the Internet (terraform/elb.tf) (aws_security_group.allow_web)
- ELB - listening on ports 80 & 443 (terraform/elb.tf) (module.elb.bizzabo-elb)
- Public route53 hosted zone and CNAME entry for the ELB (terraform/elb.tf) (aws_route53_zone.bizzabo_demo)

## Usage

```bash
$ terraform init
$ terraform plan
$ terraform apply
```

Run `terraform destroy` to remove

## Requirements

| Name | Version |
|------|---------|
| <a name="requirement_terraform"></a> [terraform](#requirement\_terraform) | >= 0.13.1 |
| <a name="requirement_aws"></a> [aws](#requirement\_aws) | >= 3.63 |
| <a name="requirement_aws"></a> [random](#requirement\_randoms) | >= 2.0 |

## ELB (elb.tf)

- creates ELB, EC2 instances and attach them together.
- creates ACM SSL certificate which can be attached to a secure listener in ELB.
- Create Security Group for public web traffic
- Integrates with vpc.tf

Based on https://github.com/terraform-aws-modules/terraform-aws-elb/tree/master/examples/complete

## Modules

| Name | Source | Version |
|------|--------|---------|
| <a name="module_acm"></a> [acm](#module\_acm) | terraform-aws-modules/acm/aws | ~> 3.0 |
| <a name="module_ec2_instances"></a> [ec2\_instances](#module\_ec2\_instances) | terraform-aws-modules/ec2-instance/aws | ~> 2.0 |
| <a name="module_elb"></a> [elb](#module\_elb) | terraform-aws-modules/elb/aws | n/a |

## Inputs

| Name | Description | Type | Default | Required |
|------|-------------|------|---------|:--------:|
| <a name="input_number_of_instances"></a> [number\_of\_instances](#input\_number\_of\_instances) | Number of instances to create and attach to ELB | `string` | `1` | no |

## Outputs

| Name | Description |
|------|-------------|
| <a name="output_elb_dns_name"></a> [elb\_dns\_name](#output\_elb\_dns\_name) | The DNS name of the ELB |
| <a name="output_elb_id"></a> [elb\_id](#output\_elb\_id) | The name of the ELB |
| <a name="output_elb_instances"></a> [elb\_instances](#output\_elb\_instances) | The list of instances in the ELB (if may be outdated, because instances are attached using elb\_attachment resource) |
| <a name="output_elb_name"></a> [elb\_name](#output\_elb\_name) | The name of the ELB |
| <a name="output_elb_source_security_group_id"></a> [elb\_source\_security\_group\_id](#output\_elb\_source\_security\_group\_id) | The ID of the security group that you can use as part of your inbound rules for your load balancer's back-end application instances |
| <a name="output_elb_zone_id"></a> [elb\_zone\_id](#output\_elb\_zone\_id) | The canonical hosted zone ID of the ELB (to be used in a Route 53 Alias record) |

## VPC (vpc.tf)

Creates set of VPC resources

based on https://github.com/terraform-aws-modules/terraform-aws-vpc/tree/master/examples/simple-vpc

There is a public and private subnet created per availability zone in addition to single NAT Gateway shared between all 3 availability zones.
This configuration uses Availability Zone IDs and Availability Zone names for demonstration purposes. Normally, you need to specify only names or IDs.

## Modules

| Name | Source | Version |
|------|--------|---------|
| <a name="module_vpc"></a> [vpc](#module\_vpc) | terraform-aws-modules/vpc/aws | n/a |
## Outputs

| Name | Description |
|------|-------------|
| <a name="output_azs"></a> [azs](#output\_azs) | A list of availability zones specified as argument to this module |
| <a name="output_nat_public_ips"></a> [nat\_public\_ips](#output\_nat\_public\_ips) | List of public Elastic IPs created for AWS NAT Gateway |
| <a name="output_private_subnets"></a> [private\_subnets](#output\_private\_subnets) | List of IDs of private subnets |
| <a name="output_public_subnets"></a> [public\_subnets](#output\_public\_subnets) | List of IDs of public subnets |
| <a name="output_vpc_cidr_block"></a> [vpc\_cidr\_block](#output\_vpc\_cidr\_block) | The CIDR block of the VPC |
| <a name="output_vpc_id"></a> [vpc\_id](#output\_vpc\_id) | The ID of the VPC |