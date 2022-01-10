#!/bin/env python

import boto3
import logging
import os 

# TODO
# Create constructor of resource with default methods e.g. get-region, list-ids
# Instantiate constructor for each (ec2, elb, etc.)
# Split into more classes

class RegionInfo:
    """
    Class that provides information about an AWS region by fetching, storing, and parsing AWS API data

    """
    region = ''
    instances = []
    load_balancers = []
    
    def __init__(self, region) -> None:
        self.region = region
        
    def get_region(self) -> str:
        return (self.region)
    
    def list_resources(self, resource_list):
        for resource in resource_list:
            print(resource)
    
    # EC2 Related functions
    
    def get_instances(self) -> list:
        """Get Instances from AWS API Effeciently

        Returns:
            list: list of instances
        """
        # Add some effeciency logic here so we don't fetch all the time
        # Balance it with data freshness, and add override for exceptions
        if not self.instances:
            self.fetch_instances()
        
        return self.instances 
    
    def fetch_instances(self) -> list:
        """Fetch instances from AWS API

        Returns:
            list: list of aws instances
        """
                      
        ec2 = boto3.client('ec2', region_name=self.region)
        response = ec2.describe_instances()
        instances = []
        for reservation in response['Reservations']:
            instances += reservation['Instances']
        self.instances = instances
    
    def get_instance_ids(self) -> list:
        """Get list of aws instances ids

        Returns:
            list: list of instance ids
        """
        instances = self.get_instances()        
        return [instance['InstanceId'] for instance in instances]

    def list_instances(self):
        """Print list of instance ids
        """
        self.list_resources(self.get_instance_ids())

    def describe_instances(self):
        instances = self.get_instances()
        """Print list of instance descriptions
        """
        
        print("InstanceId, ImageId, PrivateIpAddress")
        for instance in instances:     
            print(f"{instance['InstanceId']}, {instance['ImageId']}, {instance['PrivateIpAddress']}")

    # ELB Related functions
 
    def get_load_balancers(self) -> list:
        # Add some effeciency logic here so we don't fetch all the time
        # Balance it with data freshness, and add override for exceptions
        if not self.load_balancers:
            self.fetch_load_balancers()
            
        return self.load_balancers 
    
    def fetch_load_balancers(self) -> list:
        elb = boto3.client('elb', region_name=self.region)
        response = elb.describe_load_balancers()
        self.load_balancers = response['LoadBalancerDescriptions']
    
    def get_load_balancer_names(self) -> list:
        load_balancers = self.get_load_balancers()
        return [load_balancer['LoadBalancerName'] for load_balancer in load_balancers] 

    def list_load_balancers(self):
        self.list_resources(self.get_load_balancer_names())
        
    def describe_load_balancers(self):
        load_balancers = self.get_load_balancers()
                       
        print(f"LoadBalancerName, Scheme, DNSName")   
        for load_balancer in load_balancers:
            print(f"{load_balancer['LoadBalancerName']}, {load_balancer['Scheme']}, {load_balancer['DNSName']}")
        
if __name__ == "__main__":
    # Execute when module not intialized from import
    logging.basicConfig(level=os.environ.get("LOGLEVEL"))

    # boto3.session.Session(region_name=None, profile_name=None)
    aws = boto3.session.Session()
    sts = aws.client('sts')
    identity = sts.get_caller_identity()
    logging.debug(f'Using Identity: {identity}') 