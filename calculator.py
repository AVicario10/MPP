result = 0
intfirst_number = 0
second_number = 0

chosen_operation = input("¿Que operación quieres hacer? (+ | - | * | /)")
if chosen_operation == "+":
    first_number = input("Primer número:")
    second_number = input("Segundo número:")
    result = float(first_number) + float(second_number)
    print("{}".format(result))
elif chosen_operation == "-":
    first_number = input("Primer número:")
    second_number = input("Segundo número:")
    result = float(first_number) - float(second_number)
    print("{}".format(result))
elif chosen_operation == "*":
    first_number = input("Primer número:")
    second_number = input("Segundo número:")
    result = float(first_number) * float(second_number)
    print("{}".format(result))
elif chosen_operation == "/":
    first_number = input("Primer número:")
    second_number = input("Segundo número:")
    result = float(first_number) / float(second_number)
    print("{}".format(result))
