- VPC별 보안그룹의 이름, id, IpRanges 조회
    ```
    aws ec2 describe-security-groups --profile aws_profile \
    --query "SecurityGroups[*].{GroupName: GroupName, GroupId: GroupId, IpPermissions: IpPermissions[*].IpRanges}" \
    --filter Name=vpc-id,Values=vpc-0000000000000000
    ```