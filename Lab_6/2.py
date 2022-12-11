def oblicz_2(i, j):
    minus = i - j
    sum = i + j
    return minus, sum


a = int(input("Podaj 1 liczbe: "))
b = int(input("Podaj 2 liczbe: "))
w = oblicz_2(a, b)
print("Różnica:", w[0])
print("Summa:", w[1])

print('')

a, b = oblicz_2(62, 56)
print("Różnica:", a)
print("Summa:", b)