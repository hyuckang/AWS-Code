import boto3
import botocore

def bucket_size(aws_profile: str, bucket_name: str) -> int:
    '''
    Args:
        aws_profile: specific profile from credential file
    Returns:
        The size of all objects in the bucket (unit: GB)
    Raises:
        RuntimeError, ImportError
    '''
    try:
        ses = boto3.Session(profile_name = aws_profile)
        s3_resource = ses.resource('s3')
        s3_bucket = s3_resource.Bucket(bucket_name)

        total_byte_size = 0
        for obj in s3_bucket.objects.all():
            total_byte_size += obj.size 

        total_gb_size = total_byte_size / 1000 / 1024 / 1024
        return total_gb_size

    except botocore.exceptions.ProfileNotFound as profile_err:
        raise RuntimeError(profile_err) from profile_err

    except botocore.exceptions.ClientError as client_err:
        raise RuntimeError(client_err.response['Error']['Message']) from client_err

    except ModuleNotFoundError as module_err:
        raise ImportError(module_err) from module_err
