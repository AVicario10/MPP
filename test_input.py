h = float(input("Dime h(altura): "))
p = 101325 * ((25 - ((1 / 166) * h) / 298) ** (-9.8 / (287.05 * (1 / 166))))
print("Presión es: {}".format(p))