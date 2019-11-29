
list = [12, 2, True, [], 1.4, 'helo']

type_list = []

for data in list:
    type_list.append(type(data))

print(type_list)
