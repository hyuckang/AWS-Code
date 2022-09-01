import boto3
import botocore

def modify_volumes_to_gp3(aws_profile: str, gp2_volume_ids: list) -> list:
    '''
    Args:
        aws_profile: specific profile from credential file
    Returns:
        List of modify result
    Raises:
        RuntimeError, ImportError
    '''
    try:
        ses = boto3.Session(profile_name = aws_profile)
        ec2 = ses.client('ec2')
        
        result_list = []

        for gp2_volume_id in gp2_volume_ids:
            try:
                modify_result = ec2.modify_volume(
                                    VolumeId = gp2_volume_id,
                                    VolumeType = 'gp3'
                                )
                volume_id = modify_result['VolumeModification']['VolumeId']
                state = modify_result['VolumeModification']['ModificationState']

            except botocore.exceptions.ClientError as client_err:
                result_list.append({gp2_volume_id : client_err})
                continue

            else:
                result_list.append({volume_id : state})
        
        return result_list

    except botocore.exceptions.ProfileNotFound as profile_err:
        raise RuntimeError(profile_err) from profile_err
    except ModuleNotFoundError as module_err:
        raise ImportError(module_err) from module_err