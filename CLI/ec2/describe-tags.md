- EC2 instance에 달린 Name Tag 조회
    ```
    aws ec2 describe-tags --profile {PROFILE_NAME} \
    --filters "Name=key, Values=Name" "Name=resource-type, Values=instance"
    ```