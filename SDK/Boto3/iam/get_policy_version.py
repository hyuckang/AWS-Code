import boto3

ses = boto3.Session(profile_name='aws_profile')
iam = ses.client('iam')

iam_list_policies_resp = iam.list_policies(Scope='Local', OnlyAttached=True)

for policy in iam_list_policies_resp['Policies']:
    print(policy['PolicyName'])
    
    iam_policy_Statement = iam.get_policy_version(PolicyArn = policy['Arn'], VersionId = policy['DefaultVersionId'])
    print(iam_policy_Statement['PolicyVersion']['Document'])
    
    break