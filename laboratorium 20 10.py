
print("""Jaką operację chcesz wykonać?
1) dodawanie
2) odejmowanie
3) mnożenie
4) dzielenie
5) potęgowanie""")
i = int(input("Wpisz numer operacji: "))

a = int(input("Podaj argument 1: "))
b = int(input("Podaj argument 2: "))

if i == 1:
    print("Wynik: ", a + b)
elif i == 2:
    print("Wynik: ", a - b)
elif i == 3:
    print("Wynik: ", a * b)
elif i == 4:
    if a == 0:
        print("Błąd: Spróbuj ponownie")
        exit()
    print("Wynik: ", a / b)
elif i == 5:
    print("Wynik: ", a % b)
else:
    print("Spróbuj ponownie")
    exit()
print(" ")
