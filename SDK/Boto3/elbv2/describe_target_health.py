import boto3

ses = boto3.Session(profile_name='aws_profile')
elbv2 = ses.client('elbv2')

describe_target_groups_resp = elbv2.describe_target_groups()

for it in describe_target_groups_resp['TargetGroups']:
    Arn = it['TargetGroupArn']

    describe_target_health_resp = elbv2.describe_target_health(
        TargetGroupArn = Arn
    )

    print(describe_target_health_resp['TargetHealthDescriptions'])
