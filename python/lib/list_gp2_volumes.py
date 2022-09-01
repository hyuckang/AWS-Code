import boto3
import botocore

def list_gp2_volumes(aws_profile: str) -> list:
    '''
    Args:
        aws_profile: specific profile from credential file
    Returns:
        List of gp2 volume IDs
    Raises:
        RuntimeError, ImportError
    '''
    try:
        ses = boto3.Session(profile_name = aws_profile)
        ec2 = ses.client('ec2')
        gp2_volumes = ec2.describe_volumes(
            Filters = [
                {'Name' : 'volume-type', 'Values': ['gp2']}
            ]
        )
        
        return [gp2['VolumeId'] for gp2 in gp2_volumes['Volumes']]

    except botocore.exceptions.ProfileNotFound as profile_err:
        raise RuntimeError(profile_err) from profile_err

    except botocore.exceptions.client_err as client_err:
        raise RuntimeError(client_err.response['Error']['Message']) from client_err

    except ModuleNotFoundError as module_err:
        raise ImportError(module_err) from module_err