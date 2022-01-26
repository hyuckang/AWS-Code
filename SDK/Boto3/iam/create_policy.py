import boto3
import json

ses = boto3.Session(profile_name='aws_profile')
iam = ses.client('iam')

iam_statement = {
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": "s3:*",
            "Resource": "*"
        }
    ]
}

iam_create_policy_resp = iam.create_policy(
    PolicyName = 'create_policy_test',
    Path = '/',
    PolicyDocument = json.dumps(iam_statement),
    Description = 'create_policy_test',
    Tags = [           
    ]
)