user_sentence = input("Escribe una frase:")
len(user_sentence)

special_characters = [" ", ".", ","]
comma = 0
dot = 0
space = 0
n_special_characters = 0
n_characters = 0
no_capital = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n",
              "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
n_capital = 0


for character in user_sentence:
    if character == special_characters[2]:
        comma += 1
    if character == special_characters[1]:
        dot += 1
    if character == special_characters[0]:
        space += 1


print("Puntos: {}".format(dot))
print("Comas: {}".format(comma))
print("Espacios: {}".format(space))
print("Mayusculas: {}".format(n_capital))

