import boto3

ses = boto3.Session(profile_name='aws_profile')
iam = ses.client('iam')

iam_list_policies_resp = iam.list_policies(Scope='Local', OnlyAttached=True)

for policy in iam_list_policies_resp['Policies']:
    print(policy)