#-*-coding:utf-8-*-
try:
    from operator import itemgetter
    import boto3
except ModuleNotFoundError as Module_E:
    print(Module_E)
    exit()

try:
    ses = boto3.Session(profile_name = 'aws_profile')
except:
    print('Config Profile could not be found')
    exit()
    
iam = ses.client('iam')

list_iam_user = sorted(iam.list_users()['Users'], key=itemgetter('CreateDate'))
    

print('# IAM USER & GROUP')
print('{0:<15} | {1:<25} | {2:<15}'.format('IAM USER', 'CreateDate', 'Groups'))
for user in list_iam_user:
    print('{0:<15} | {1} | '.format(user['UserName'], user['CreateDate']), end = '')

    user_groups = iam.list_groups_for_user(UserName = user['UserName'])['Groups']
    for group in user_groups:
        print('{0:<15} {1:<3}'.format(group['GroupName'], ' '), end = '')
    print('')