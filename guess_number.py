number_to_guess = 0
initial_number = 0

initial_number = input("Número a adivinar:")
print ("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")


while number_to_guess != initial_number:
    number_to_guess = input("Adivina el numero:")
    if number_to_guess == initial_number:
        print("¡Has adivinado en número!")

