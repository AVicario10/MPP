user_numbers = []

while len(user_numbers) < 10:
    user_numbers.append(int(input("Dime un numero: ")))

print(float((user_numbers[0]+user_numbers[1]+user_numbers[2]+user_numbers[3]+user_numbers[4]+user_numbers[5]
             + user_numbers[6]+user_numbers[7]+user_numbers[8]+user_numbers[9]) / len(user_numbers)))

