# Terraform Implementation

## AWS Infrastructure as Code 

Infrastructure as code for AWS was created using Terraform and includes the following

### VPC

- VPC with two public and private subnets (terraform/vpc.tf)
- Route tables for each subnet (terraform/vpc.tf)

### ELB

- Security Group to allow port 80 and 443 from the Internet (terraform/elb.tf)
- ELB - listening on ports 80 & 443 (terraform/elb.tf)
- Public route53 hosted zone and CNAME entry for the ELB (terraform/elb.tf)

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

## Simple VPC (vpc.tf)

Creates set of VPC resources

VPC Section based on https://github.com/terraform-aws-modules/terraform-aws-vpc/tree/master/examples/simple-vpc

There is a public and private subnet created per availability zone in addition to single NAT Gateway shared between all 3 availability zones.
This configuration uses Availability Zone IDs and Availability Zone names for demonstration purposes. Normally, you need to specify only names or IDs.

## Modules

| Name | Source | Version |
|------|--------|---------|
| <a name="module_vpc"></a> [vpc](#module\_vpc) | ../../ | n/a |
## Outputs

| Name | Description |
|------|-------------|
| <a name="output_azs"></a> [azs](#output\_azs) | A list of availability zones specified as argument to this module |
| <a name="output_nat_public_ips"></a> [nat\_public\_ips](#output\_nat\_public\_ips) | List of public Elastic IPs created for AWS NAT Gateway |
| <a name="output_private_subnets"></a> [private\_subnets](#output\_private\_subnets) | List of IDs of private subnets |
| <a name="output_public_subnets"></a> [public\_subnets](#output\_public\_subnets) | List of IDs of public subnets |
| <a name="output_vpc_cidr_block"></a> [vpc\_cidr\_block](#output\_vpc\_cidr\_block) | The CIDR block of the VPC |
| <a name="output_vpc_id"></a> [vpc\_id](#output\_vpc\_id) | The ID of the VPC |