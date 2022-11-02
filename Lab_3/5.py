n = int(input("Ile studentów w grupie: "))
x = 1
suma = 0
while x <= n:
    # print("Podaj liczbę punktów dla studenta", x)
    # s = float(input())
    s = float(input(f"Podaj liczbę punktów studenta {x}: "))
    suma += s
    x += 1

print("Średnią liczbę punktów: ", suma/n)
