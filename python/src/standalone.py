#!/bin/env python

import boto3
import logging
import os

# Get information

def get_instances(region: str) -> list:
    ec2 = boto3.client('ec2', region_name=region)
    response = ec2.describe_instances()
    instances = []
    for reservation in response['Reservations']:
        instances += [instance['InstanceId'] for instance in reservation['Instances']]
    return instances

def get_load_balancers(region:str) -> list:
    elb = boto3.client('elb', region_name=region)
    response = elb.describe_load_balancers()
    return [load_balancer['LoadBalancerName'] for load_balancer in response['LoadBalancerDescriptions']] 

# Describe Information

def describe_instances(region: str, instances: list):
    ec2 = boto3.client('ec2', region_name=region)
    response = ec2.describe_instances( InstanceIds=instances)
    
    print("InstanceId, ImageId, PrivateIpAddress")
    for reservation in response['Reservations']:
       for instance in reservation['Instances']:
            print(f"{instance['InstanceId']}, {instance['ImageId']}, {instance['PrivateIpAddress']}")

def describe_load_balancers(region, load_balancers):
    elb = boto3.client('elb', region_name=region)
    response = elb.describe_load_balancers(LoadBalancerNames=load_balancers)
    
    print(f"LoadBalancerName, Scheme, DNSName")   
    for load_balancer in response['LoadBalancerDescriptions']:
        print(f"{load_balancer['LoadBalancerName']}, {load_balancer['Scheme']}, {load_balancer['DNSName']}")

if __name__ == "__main__":
    # Execute when module not intialized from import
    logging.basicConfig(level=os.environ.get("LOGLEVEL"))

    # boto3.session.Session(region_name=None, profile_name=None)
    aws = boto3.session.Session()
    sts = aws.client('sts')
    identity = sts.get_caller_identity()
    logging.debug(f'Using Identity: {identity}') 
    
    region = os.environ.get('AWS_REGION')
    load_balancers = get_load_balancers(region)
    instances = get_instances(region)
    
    describe_instances(region, instances)
    describe_load_balancers(region, load_balancers)