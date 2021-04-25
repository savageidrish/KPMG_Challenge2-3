#!/bin/bash

#To retrieve metadata of EC2 instance in JSON format

curl http://169.254.169.254/latest/dynamic/instance-identity/document



#To retrieve a specific data for example - regoin of the EC2 instance

curl http://169.254.169.254/latest/dynamic/instance-identity/document | jq -r .region