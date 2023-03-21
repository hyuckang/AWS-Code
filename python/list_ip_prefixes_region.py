import requests

region_name = 'ap-northeast-2'
ip_prefixes = requests.get('https://ip-ranges.amazonaws.com/ip-ranges.json').json()['prefixes']
region_ip_prefixes = [ip for ip in ip_prefixes if ip['region'] == region_name ]

print(region_ip_prefixes)
