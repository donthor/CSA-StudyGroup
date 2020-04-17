import ipaddress

while True:
    ipstring = input('Enter IP Address (Type x to End): ')
    if ipstring.lower() == 'x':
        break
    try:
        ipadd = ipaddress.IPv4Address(ipstring)
        print(f'{ipadd} is a Valid IP Address')

    except ValueError:
        print(f'{ipstring} is not a Valid IP Address')



