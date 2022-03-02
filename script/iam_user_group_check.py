import boto3
from operator import itemgetter

ses = boto3.Session(profile_name='aws_profile')
iam = ses.client('iam')

resp = iam.list_users()['Users']
resp_sorted_by_datetime = sorted(resp, key=itemgetter('CreateDate'))

for user in resp_sorted_by_datetime:
    user_name = user['UserName']
    create_date = user['CreateDate']
    user_groups = iam.list_groups_for_user(UserName=user_name)['Groups']

    print("--------------------------------------------")
    print('user_name : {0}'.format(user['UserName']))
    print('create_date : {0}'.format(user['CreateDate']))
    
    for group in user_groups:
        print('group : {0}'.format(group['GroupName']))
