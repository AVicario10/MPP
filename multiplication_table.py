number = input("Dime el numero que quieres multiplicar:")

first_n = 10

while first_n != 0:
    print("{} x {} = {}".format(number, first_n, (int(number) * int(first_n))))
    first_n -= 1

