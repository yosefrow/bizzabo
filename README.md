

# DevOps Eng @ Bizzabo - Assignment 

The Challenge Below is a multiple steps challenge. 
Please try to implement as many features as possible and provide proper description wherever applicable with your git projects. To test your tool, a free 
Amazon account should be created (if you don't already have one). 

## Requirements

### AWS Infrastructure as Code 

Write using any IAC engine (Terraform is preferred but CloudFormation/Ansible are also ok) to create the below AWS components: 

- VPC with two public and private subnets 
- Route tables for each subnet 
- Security Group to allow port 80 and 443 from the Internet 
- ELB - listening on ports 80 & 443 
- Public route53 hosted zone and CNAME entry for the ELB 

### AWS API 

Create a script using any preferred programming language (Python, Node.js, Java, etc.) to perform the following activities: 
- List AWS services being used region wise 
- List each service in detail, like EC2, RDS etc. 

### Notes 

Try to think “big” and consider the following guidelines: 
- Try to design and implement your solution as you would do in a real production code. Show us how you create a clean, maintainable code that does awesome stuff. Build something 
that we'd be happy to contribute to. This is not a programming contest where dirty hacks win the game. 
- Feel free to add more features! Really, we're curious about how your mind works. We'd expect the same if you worked with us. 
- Documentation and maintainability is a plus. 
- Commit all artifacts/scripts to Github and write your explanations and documentation in a README file 

## Implementation

### AWS Infrastructure as Code 

Infrastructure as code for AWS was created using Terraform and includes the following

- VPC with two public and private subnets (terraform/vpc.tf)
- Route tables for each subnet (terraform/vpc.tf)
- Security Group to allow port 80 and 443 from the Internet (terraform/security.tf)
- ELB - listening on ports 80 & 443 (terraform/elb.tf)
- Public route53 hosted zone and CNAME entry for the ELB (terraform/dns.tf)

### AWS API 

The script was create dusing Python and performs the following activities: 

- List AWS services being used region wise (python/list-services.py)
- List each service in detail, like EC2, RDS etc. (python/describe-services.py)

### Notes 

- GitHub repo: 
