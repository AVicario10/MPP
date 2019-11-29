number = int(input('Tell me a number'))

list = [1, 2 , 3, 4, 5, 6, 7, 8, 9]

result = []

for data in list:
    result.append((number * int(data)))

print(result)
