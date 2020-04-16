mylist = []
mxcount = 0
mrcount = 0
mscount = 0
msversion = 11.31
mrversion = 26.6
mxversion = 14.40
with open('merakiinvlist','r') as version_file:
    for version_output in version_file:
        
        data = version_output.strip().split(',')
        data = [x.strip(' ') for x in data]
       
        mylist.append(data)
        
print(mylist)
for device in mylist:
    if device[2][:6] == 'switch' and float(device[2][7:12].replace('-','.')) < msversion:
        mscount += 1
    elif device[2][:8] == 'wireless' and float(device[2][9:13].replace('-','.')) < mrversion:
        mrcount += 1
    elif device[2][:5] == 'wired' and float(device[2][6:11].replace('-','.')) < mxversion:
        mxcount += 1
print(f'Total switches to be upgraded: {mscount}')
print(f'Total APs to be upgraded: {mrcount}')
print(f'Total Security Appliances to be upgraded: {mxcount}')