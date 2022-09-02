import boto3
import botocore

def list_acm(aws_profile: str) -> list:
    '''
    Args:
        aws_profile: specific profile from credential file
    Returns:
        List of dictionaries containing acm certificate information
    Raises:
        RuntimeError, ImportError
    '''
    try:
        ses = boto3.Session(profile_name = aws_profile)
        acm = ses.client('acm')
        acm_summary_list = acm.list_certificates()['CertificateSummaryList']

        acm_list = [
            acm.describe_certificate(CertificateArn = acm_summary['CertificateArn'])['Certificate']
            for acm_summary in acm_summary_list
        ]

        return acm_list

    except botocore.exceptions.ProfileNotFound as profile_err:
        raise RuntimeError(profile_err) from profile_err

    except botocore.exceptions.ClientError as client_err:
        raise RuntimeError(client_err.response['Error']['Message']) from client_err

    except ModuleNotFoundError as module_err:
        raise ImportError(module_err) from module_err

if __name__ == '__main__':
    aws_profile = input('Input aws profile : ')
    print(list_acm(aws_profile))