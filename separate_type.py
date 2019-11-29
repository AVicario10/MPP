list = ["pedo", 23, "culo", 2354, "caca", 4]
strings = []
ints = []


for data in list:
    if type(data) == str:
        strings.append(data)
    if type(data) == int:
        ints.append(data)

print(ints)
print(strings)
