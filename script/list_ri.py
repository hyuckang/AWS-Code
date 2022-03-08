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
    print("Config Profile could not be found")
    exit()

ec2 = ses.client('ec2')
rds = ses.client('rds')

list_ec2_ri = ec2.describe_reserved_instances(
    Filters = [
        {   'Name' : 'state', 'Values' : ['active']     }
    ]
)
list_rds_ri = rds.describe_reserved_db_instances(
    Filters = [
        {   'Name' : 'status', 'Values' : ['active']    }
    ]
)

list_ec2_ri = sorted(list_ec2_ri['ReservedInstances'], key=itemgetter('Start'))
list_rds_ri = sorted(list_rds_ri['ReservedDBInstances'], key=itemgetter('StartTime'))

print('# EC2 RI #')
if list_ec2_ri:
    print('{0:<15} | {1:<20} | {2:<25} | {3:<25} | {4:<10} | {5:<3}'
        .format('InstanceType', 'ProductDescription', 'Start', 'End', 'Price', 'Count'))

    for ec2_ri in list_ec2_ri:
        print('{0:<15} | {1:<20} | {2} | {3} | {4:<10} | {5:<3}'
            .format(ec2_ri['InstanceType'], ec2_ri['ProductDescription'], ec2_ri['Start'], ec2_ri['End'], ec2_ri['FixedPrice'], ec2_ri['InstanceCount']))
else:
    print("EC2 RI List is not exist")

print('# RDS RI #')
if list_rds_ri:
    print('{0:<15} | {1:<20} | {2:<25} | {3:<10} | {4:<3}'
        .format('InstanceType', 'ProductDescription', 'Start', 'Price', 'Count'))

    for rds_ri in list_rds_ri:
        print('{0:<15} | {1:<20} | {2} | {3:<10} | {4:<3}'
            .format(rds_ri['DBInstanceClass'], rds_ri['ProductDescription'], rds_ri['StartTime'], rds_ri['FixedPrice'], rds_ri['DBInstanceCount']))
else:
    print("RDS RI LIST is not exist")
