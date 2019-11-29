repeat = 1
vowels = ('a', 'e', 'o', 'u')
while repeat > 0:
    user_sentence = input("Say something:")
    a = user_sentence.replace("a", "i")
    e = a.replace("e", "i")
    o = e.replace("o", "i")
    new_inp = o.replace("u", "i")
    print(new_inp)
