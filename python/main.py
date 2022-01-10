#!/bin/env python

import boto3
import logging
import os

def get_instances(region):
    print(f'region_name: {region}')
    ec2 = boto3.resource('ec2', region_name=region)
    response = ec2.meta.client.describe_instances()
    instances = []
    for reservation in response['Reservations']:
        instances += [instance['InstanceId'] for instance in reservation['Instances']]
    return instances

def describe_instances(region):
    print(f'region_name: {region}')
    ec2 = boto3.resource('ec2', region_name=region)
    response = ec2.meta.client.describe_instances()
    instances = []
    for reservation in response['Reservations']:
        instances += [instance['InstanceId'] for instance in reservation['Instances']]
    return instances
            
def get_load_balancers(region):
    print(f'region_name: {region}')
    elb = boto3.client('elb', region_name=region)
    response = elb.describe_load_balancers()
    return [description['LoadBalancerName'] for description in response['LoadBalancerDescriptions']] 

def get_load_balancers(region):
    print(f'region_name: {region}')
    elb = boto3.client('elb', region_name=region)
    response = elb.describe_load_balancers()
    return [description['LoadBalancerName'] for description in response['LoadBalancerDescriptions']] 

if __name__ == "__main__":
    # Execute when module not intialized from import
    logging.basicConfig(level=os.environ.get("LOGLEVEL"))

    # boto3.session.Session(region_name=None, profile_name=None)
    aws = boto3.session.Session()
    sts = aws.client('sts')
    identity = sts.get_caller_identity()
    logging.debug(f'Using Identity: {identity}') 
    
    region = os.environ.get('AWS_REGION')
    print(get_load_balancers(region))
    print(get_instances(region))
    
    
    