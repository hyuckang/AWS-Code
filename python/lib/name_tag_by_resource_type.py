from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import boto3

def name_tag_by_resource_type(aws_profile: str, resource_type: str) -> dict:
    """
    Args:
        aws_profile: specific profile from credential file.
        resource_type: resource type such as security-group, route-table, instance, subnet, vpc
    
    Returns:
        A dictionary with resource id as key and name tag as value.

    Raises:
        ModuleNotFoundError
    """
    ses = boto3.Session(profile_name = aws_profile)
    ec2 = ses.client('ec2')

    tags = ec2.describe_tags(
        Filters = [
            {'Name' : 'resource-type', 'Values' : [resource_type]},
            {'Name' : 'key', 'Values' : ['Name']}
        ]
    )

    return {tag['ResourceId']:tag['Value'] for tag in tags['Tags']}
