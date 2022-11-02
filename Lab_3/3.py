'''x = int(input("Podaj liczbe: "))

while x >= 0:
    x = int(input("Podaj liczbe: "))
    if x < 0:
        print("Koniec bo liczba jest ujemna")
        break
'''

while True:
    x = int(input("Podaj liczbe: "))
    if x < 0:
        print("Koniec bo liczba jest ujemna")
        break