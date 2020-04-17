import ipaddress
import json

with open('JSONdata') as f:
    data = json.load(f)
for i in data:

    try:
        ipadd = ipaddress.IPv4Address(i['lanIp'])
        print(f'{ipadd} is a Valid IP Address for Serial #{i["serial"]}')

    except ValueError:
        print(f'{i["lanIp"]} is not a Valid IP Address for Serial #{i["serial"]}')



