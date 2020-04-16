mylist = []
uniquelist = []
serialnumbers = set()

with open('dirtylist','r') as version_file:
    for version_output in version_file:
        
        data = version_output.strip().split(',')
        data = [x.strip(' ') for x in data]
        mylist.append(data)
        
print(len(mylist))
for device in mylist:
    print(device)
    if device[0] in serialnumbers:
        print('duplicate!')
        continue
    else:
        uniquelist.append(device)
    serialnumbers.add(device[0])
print(serialnumbers)
print('')
print(uniquelist)
print(len(uniquelist))
