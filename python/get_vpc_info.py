import boto3
import sys

def get_vpc_info(vpc_id):
    ec2 = boto3.client('ec2', region_name = 'ap-northeast-2')

    # Get VPC information
    vpc_response = ec2.describe_vpcs(VpcIds=[vpc_id])
    vpc = vpc_response['Vpcs'][0]
    vpc_name = next((tag['Value'] for tag in vpc.get('Tags', []) if tag['Key'] == 'Name'), 'N/A')

    print("# VPC")
    print(f"\t- vpc_name: {vpc_name}")
    print(f"\t- vpc_id: {vpc_id}")
    print(f"\t- vpc_cidr: {vpc['CidrBlock']}")

    # Get Subnet information
    subnet_response = ec2.describe_subnets(Filters=[{'Name': 'vpc-id', 'Values': [vpc_id]}])
    subnets = subnet_response['Subnets']
    
    # Sort subnets by name
    subnets.sort(key=lambda x: next((tag['Value'] for tag in x.get('Tags', []) if tag['Key'] == 'Name'), 'N/A'))
    
    print("# Subnets")
    for subnet in subnets:
        subnet_name = next((tag['Value'] for tag in subnet.get('Tags', []) if tag['Key'] == 'Name'), 'N/A')
        subnet_id = subnet['SubnetId']
        
        # Get routing information
        route_tables = ec2.describe_route_tables(Filters=[{'Name': 'association.subnet-id', 'Values': [subnet_id]}])
        internet_routing = '-'
        if route_tables['RouteTables']:
            for route in route_tables['RouteTables'][0]['Routes']:
                if route.get('DestinationCidrBlock') == '0.0.0.0/0':
                    internet_routing = route.get('GatewayId', route.get('NatGatewayId', '-'))
                    break

        print("\t-----")
        print(f"\t- subnet_name: {subnet_name}")
        print(f"\t- subnet_id: {subnet_id}")
        print(f"\t- vpc_cidr: {subnet['CidrBlock']}")
        print(f"\t- internet_routing: {internet_routing}")

    # Get NAT Gateway information
    natgw_response = ec2.describe_nat_gateways(Filters=[{'Name': 'vpc-id', 'Values': [vpc_id]}])
    print("# NAT GWS")
    for natgw in natgw_response['NatGateways']:
        natgw_name = next((tag['Value'] for tag in natgw.get('Tags', []) if tag['Key'] == 'Name'), 'N/A')
        print(f"\t- natgw_name: {natgw_name}")
        print(f"\t- natgw_id: {natgw['NatGatewayId']}")
        print(f"\t- subnet_id: {natgw['SubnetId']}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <vpc_id>")
        sys.exit(1)
    
    vpc_id = sys.argv[1]
    get_vpc_info(vpc_id)
