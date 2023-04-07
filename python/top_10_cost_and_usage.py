import boto3

ce = boto3.client('ce')

service_cost_response = ce.get_cost_and_usage(
    TimePeriod={
        'Start': '2023-03-01',
        'End': '2023-03-31'
    },
    Granularity='MONTHLY',
    Metrics=['AmortizedCost'],
    GroupBy=[
        {
            'Type': 'DIMENSION',
            'Key': 'SERVICE'
        }
    ],
    Filter={
        'Dimensions': {
            'Key': 'LINKED_ACCOUNT',
            'Values': [
                '000000000000'
            ]
        }
    }
)

service_costs = service_cost_response['ResultsByTime'][0]['Groups']
sorted_service_costs = sorted(service_costs, key=lambda x: float(x['Metrics']['AmortizedCost']['Amount']), reverse=True)[:10]

for cost in sorted_service_costs:
    service, amount_cost = cost['Keys'][0], cost['Metrics']['AmortizedCost']['Amount']
    print(f'{service} \t AmountCost : {amount_cost}')

    usage_cost_response = ce.get_cost_and_usage(
        TimePeriod={
            'Start': '2023-03-01',
            'End': '2023-03-31'
        },
        Granularity='MONTHLY',
        Metrics=['AmortizedCost'],
        GroupBy=[
            {
                'Type' : 'DIMENSION',
                'Key' : 'USAGE_TYPE'
            }
        ],
        Filter={
            'And': [
                {
                    "Dimensions": {
                        'Key': 'LINKED_ACCOUNT',
                        'Values': ['000000000000']
                    }
                },
                {
                    "Dimensions": {
                        "Key": "SERVICE",
                        "Values": [service]
                    }
                }
            ]
        }
    )
    usage_cost = usage_cost_response['ResultsByTime'][0]['Groups']
    sorted_usage_cost = sorted(usage_cost, key=lambda x: float(x['Metrics']['AmortizedCost']['Amount']), reverse=True)[:10]

    for usage in sorted_usage_cost:
        usage, usage_cost = usage['Keys'][0], usage['Metrics']['AmortizedCost']['Amount']
        print(f'\t{usage} \t{usage_cost}')

