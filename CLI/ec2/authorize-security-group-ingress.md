- 출발지 172.16.3.0/24인 SSH 트래픽을 허용하는 인바운드를 추가하고, Description으로 "SSH_InfraTeam"을 추가한다.
    ```
    aws ec2 authorize-security-group-ingress \
    --profile {PROFILE_NAME} \
    --group-id {Security-Group-ID} \
    --ip-permissions IpProtocol=tcp,FromPort=22,ToPort=22,\
    IpRanges='[{CidrIp=172.16.3.0/24,Description="SSH_InfraTeam"}]'
    ```
