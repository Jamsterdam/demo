# myDict = {"key": "value", "key2": "value"}
#
# print(myDict)
#
# print(myDict['key'])

# access dictionary keys
phones = {'m1': 1000, 'm2': 2003}
for phone in phones:
    print(phone)
m1Price = phones['m1']
print(m1Price)

# change a key value
phones['m1'] = 500
print(m1Price)

phones.clear()
print(phones)