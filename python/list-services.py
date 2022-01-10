#!/bin/env python

import boto3
import logging
import os

def get_region_services(boto_identity):
    aws = boto_identity

if __name__ == "__main__":
    logging.basicConfig(level=os.environ.get("LOGLEVEL"))
    # Execute when module not intialized from import
    logging.warning('Starting program!') 

    # boto3.session.Session(region_name=None, profile_name=None)
    aws = boto3.session.Session()
    sts = aws.client('sts')
    identity = sts.get_caller_identity()
    logging.debug(f'Using Identity: {identity}') 