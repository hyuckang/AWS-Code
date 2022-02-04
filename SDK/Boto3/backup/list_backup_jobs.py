import boto3

ses = boto3.Session(profile_name = 'aws_profile')
backup = ses.client('backup')

list_backup_jobs_resp = backup.list_backup_jobs(
    ByState = 'FAILED'
)

print(list_backup_jobs_resp['BackupJobs'])