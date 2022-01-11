# Python Implementation
## AWS API - Requirement

The script was created using Python and performs the following activities: 

- List AWS services being used region wise (python/list-services.py)
- List each service in detail, like EC2, RDS etc. (python/describe-services.py)

## Setup Environment

This application uses Python virtual environment to ensure consistency and stability
It can optionally be deployed to a container using the Dockerfile which is included

### Deploy python environment

`setup.sh`

### Run Application in Docker

`build.sh`
`run.sh`

### Additional Info

As well as the default class-based application, there is also a standalone version available,
though may be a bit out of date compared to the class based version

### TODO

1. create a parent constructor for resource types
2. Add a class for each resource type in the region
3. Add Helm Chart / Kubernetes deployment, possibly in cronjob format
4. Add more detailed / customizable description fields and formats

