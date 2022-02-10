import boto3
import datetime

ses = boto3.Session(profile_name='aws_profile')
cloudwatch = ses.client('cloudwatch')

metric_statistics = cloudwatch.get_metric_statistics(
        Namespace = 'AWS/RDS',
        MetricName = 'CPUUtilization',
        Dimensions = [
            {
                "Name": "DBInstanceIdentifier",
                "Value": "rds-instance"    
            }
        ],
        StartTime = datetime.datetime.utcnow() - datetime.timedelta(seconds = 600),
        EndTime = datetime.datetime.utcnow(),
        Period = 600,
        Statistics = ['Average'],
        Unit = 'Percent'
)
