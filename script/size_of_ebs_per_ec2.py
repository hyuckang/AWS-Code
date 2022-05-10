import boto3
import botocore

def size_of_ebs_per_ec2(aws_profile: str) -> dict:
    '''
    Args:
        aws_profile: specific profile from credential file
    Returns:
        A dictionary where the ec2 instance is the key and the sum of the size ebs is the value.
    Raises:
        RuntimeError, ImportError
    '''
    try:
        ses = boto3.Session(profile_name = aws_profile)
        ec2 = ses.client('ec2')
        resp = ec2.describe_volumes(
            Filters = [
                {'Name' : 'status', 'Values' : ['in-use']},
                {'Name' : 'multi-attach-enabled', 'Values' : ['false']}
            ]
        )

        size_of_ebs = {}
        for ebs in resp['Volumes']:
            ec2_instance_id = ebs['Attachments'][0]['InstanceId']

            if (ec2_instance_id in size_of_ebs):
                size_of_ebs[ec2_instance_id] += ebs['Size']
            else:
                size_of_ebs[ec2_instance_id] = (0 + ebs['Size'])

        return size_of_ebs

    except botocore.exceptions.ProfileNotFound as profile_err:
        raise RuntimeError(profile_err) from profile_err

    except botocore.exceptions.ClientError as client_err:
        raise RuntimeError(client_err.response['Error']['Message']) from client_err

    except ModuleNotFoundError as module_err:
        raise ImportError(module_err) from module_err
