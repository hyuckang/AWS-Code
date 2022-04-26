from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import boto3
from name_tag_by_resource_type import name_tag_by_resource_type


def list_ec2_instances(aws_profile: str) -> list:
    '''
    Args:
        aws_profile: specific profile from credential file.
    Returns:
        List of dictionaries with keys VpcNameTag, SubnetIdNameTag, InstanceNameTag, PrivateIpAddress, etc.
    Raises:
        ModuleNotFoundError
    '''
    list_ec2 = []
    ses = boto3.Session(profile_name = aws_profile)
    ec2 = ses.client('ec2')
    ec2_describes = ec2.describe_instances()

    vpc_nametags = name_tag_by_resource_type(aws_profile, 'vpc')
    subnet_nametags = name_tag_by_resource_type(aws_profile, 'subnet')
    instance_nametags = name_tag_by_resource_type(aws_profile, 'instance')

    for ec2_desc in ec2_describes['Reservations']:
        desc = {}
        desc['VpcNameTag'] = vpc_nametags[ec2_desc['Instances'][0]['VpcId']]
        desc['SubnetIdNameTag'] = subnet_nametags[ec2_desc['Instances'][0]['SubnetId']]
        desc['InstanceNameTag'] = instance_nametags[ec2_desc['Instances'][0]['InstanceId']]
        desc['InstanceId'] = ec2_desc['Instances'][0]['InstanceId']
        desc['InstanceType'] = ec2_desc['Instances'][0]['InstanceType']
        desc['PrivateIpAddress'] = ec2_desc['Instances'][0]['PrivateIpAddress']
        desc['PublicIpAddress'] = ec2_desc['Instances'][0]['PublicIpAddress'] if 'PublicIpAddress' in ec2_desc['Instances'][0] else '-'

        list_ec2.append(desc)

    return list_ec2
