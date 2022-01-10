#!/bin/env python

import boto3
import logging
import os
from modules.RegionInfo import RegionInfo as RegionInfo

def show_identity():
    # boto3.session.Session(region_name=None, profile_name=None)
    aws = boto3.session.Session()
    sts = aws.client('sts')
    identity = sts.get_caller_identity()
    logging.debug(f'Using Identity: {identity}') 

if __name__ == "__main__":
    # Execute when module not intialized from import
    logging.basicConfig(level=os.environ.get("LOGLEVEL"))

    show_identity()
    
    region = os.environ.get('AWS_DEFAULT_REGION')
    region_info=RegionInfo(region)
    
    # Show Resource 1
    print(f"List Instances for {region}:")
    print('------------------------------')
    region_info.list_instances()
    print('\n')
    print(f"Describe Instances for {region}:")
    print('------------------------------')
    region_info.describe_instances()
    print('\n')
    
    
    # Show Resource 2
    print(f"List Load Balancers for {region}:")
    print('------------------------------')
    region_info.list_load_balancers()
    print('\n')
    print(f"Describe Load Balancers for {region}:")
    print('------------------------------')
    region_info.describe_load_balancers()    
    print('\n')