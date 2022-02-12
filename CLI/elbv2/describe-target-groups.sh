aws elbv2 describe-target-groups --profile aws_profile \
--query "TargetGroups[*].{TargetGroupArn : TargetGroupArn}" \
--output text
