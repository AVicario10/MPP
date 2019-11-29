repeat = 1
x = 0
vowels = ['a', 'e', 'i', 'o', 'u']
while repeat > 0:
    user_sentence = input("Say something:")
    for letter in vowels:
        x = x + 1
        new_inp = user_sentence.replace(str(vowels), str(x))

    print(new_inp)
