import boto3
import botocore

def list_failed_backup_jobs(aws_profile: str) -> list:
    try:
        ses = boto3.Session(profile_name = 'aws_profile')
        backup = ses.client('backup')
        failed_backup_jobs = backup.list_backup_jobs(
                                ByState = 'FAILED'
                            )
        return failed_backup_jobs['BackupJobs']
        
    except botocore.exceptions.ProfileNotFound as profile_err:
        raise RuntimeError(profile_err) from profile_err

    except botocore.exceptions.client_err as client_err:
        raise RuntimeError(client_err.response['Error']['Message']) from client_err

    except ModuleNotFoundError as module_err:
        raise ImportError(module_err) from module_err

if __name__ == '__main__':
    aws_profile = input('Input aws profile : ')
    print(list_failed_backup_jobs(aws_profile))