list = ["pedo", 23, "culo", 2354, "caca", 4]
strings = []
ints = []


for data in list:
    if data == str:
        strings.append(data)
    if data == int:
        ints.append(data)

print(ints)
print(strings)
