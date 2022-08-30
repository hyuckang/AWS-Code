import boto3
import botocore

def update_iam_user_passwd(aws_profile: str, iam_username: str, new_password: str) -> str:
    '''
    Args:
        aws_profile: specific profile from credential file
        iam_username : Username to change password
        new_password : New password to apply
    Returns:
        Error message or Password change result message
    Raises:
        RuntimeError
    '''
    try:
        ses = boto3.Session(profile_name = aws_profile)
        iam = ses.client('iam')
        resp = iam.update_login_profile(
            UserName = iam_username,
            Password = new_password,
            PasswordResetRequired = True
        )

        if (resp['ResponseMetadata']['HTTPStatusCode'] == 200):
            return f"Success in changing password to '{new_password}'"
        else:
            return "Failed to change password"

    except botocore.exceptions.ProfileNotFound as profile_err:
        raise RuntimeError(profile_err) from profile_err

    except botocore.exceptions.ClientError as client_err:
        raise RuntimeError(client_err.response['Error']['Message']) from client_err
