# Terraform Implementation

## AWS Infrastructure as Code 

Infrastructure as code for AWS was created using Terraform and includes the following

- VPC with two public and private subnets (terraform/vpc.tf)
- Route tables for each subnet (terraform/vpc.tf)
- Security Group to allow port 80 and 443 from the Internet (terraform/security.tf)
- ELB - listening on ports 80 & 443 (terraform/elb.tf)
- Public route53 hosted zone and CNAME entry for the ELB (terraform/dns.tf)