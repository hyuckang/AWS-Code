import boto3
import botocore

def list_bucket_name(aws_profile: str) -> list:
    '''
    Args:
        aws_profile: specific profile from credential file
    Returns:
        list of bucket names
    Raises:
        RuntimeError, ImportError
    '''
    try:
        ses = boto3.Session(profile_name = aws_profile)
        s3 = ses.client('s3')
        bucket_name_list = [bucket['Name'] for bucket in s3.list_buckets()['Buckets']]
        return bucket_name_list

    except botocore.exceptions.ProfileNotFound as profile_err:
        raise RuntimeError(profile_err) from profile_err

    except botocore.exceptions.ClientError as client_err:
        raise RuntimeError(client_err.response['Error']['Message']) from client_err

    except ModuleNotFoundError as module_err:
        raise ImportError(module_err) from module_err
