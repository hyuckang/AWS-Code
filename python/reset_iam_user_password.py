from lib import update_iam_user_passwd

if '__name__' == '__main__':
    aws_profile = input('Input aws profile : ')
    iam_username = input('Input iam username : ')
    print(update_iam_user_passwd(aws_profile, iam_username, 'Password12#$'))