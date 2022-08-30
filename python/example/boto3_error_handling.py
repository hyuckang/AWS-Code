import boto3
import botocore

# Profile
try:
    ses = boto3.Session(profile_name = 'aws_profile')
    iam = ses.client('iam')
except botocore.exceptions.ProfileNotFound as profile_err:
    raise RuntimeError(profile_err) from profile_err

# Client error handling - [1]
try:
    user_info = iam.get_user(
        UserName = 'iam_username_1'
    )
except iam.exceptions.NoSuchEntityException as no_such_entity_err:
    raise ValueError('No such Entity iam_username_1') from no_such_entity_err

# Client error handling - [2]
try:
    user_info = iam.get_user(
        UserName = 'iam_username_2'
    )
except botocore.exceptions.ClientError as client_err:
    raise RuntimeError(client_err.response['Error']['Message']) from client_err
