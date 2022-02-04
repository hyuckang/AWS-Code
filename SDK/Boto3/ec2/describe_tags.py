import boto3

ses = boto3.Session(profile_name = 'aws_profile')
ec2 = ses.client('ec2')

describe_tags_resp = ec2.describe_tags(
    Filters = [
        {'Name' : 'key', 'Values' : ['Name']},
        {'Name' : 'resource-type', 'Values' : ['instance']}
    ]
)

print(describe_tags_resp['Tags'])