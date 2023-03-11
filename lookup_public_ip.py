import requests

public_ip_lookup_services: list = [
    'http://checkip.amazonaws.com/',
    'http://ip-api.com/json/',
    'https://ifconfig.me/ip',
]

for service in public_ip_lookup_services:
    response = requests.get(service)
    ip_address = response.text
    print(f'''
{service}
{ip_address}
''')
