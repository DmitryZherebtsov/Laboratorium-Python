import random
# punkty = []

# for i in range(15):
#     p = random.uniform(0, 50)
#     p = round(p,2)
#     # punkty.append(round(p))
#     punkty.append(p)

punkty = [round(random.uniform(0, 50),2) for a in range(15)]

print(punkty)
print(f'Minimalne: {min(punkty)}')
print(f'Maxymalnie: {max(punkty)}')
a = float(input("Wybierz liczbę: "))
if a in punkty:
    print("Liczbę ma index: ", punkty.index(a))
else:
    print("Liczbę nie występuje na liście")


sum = 0
for i in range(len(punkty)):
    sum = sum + punkty[i]
    i = i + 1
print('Sum:', round(sum))

srednia = sum/15
print("Średnia: ", round(srednia))

powyzej = []
# powyzej = sum(punkty)/15
for s in punkty:
    if s>srednia:
        powyzej.append(s)
print("Liczbę wartości powyżej średni: ", len(powyzej), powyzej)


# punkty=[round(random.uniform(0,50),2) for a in range(15)]
# print(punkty)
# print(f'Wartośc minimalna wynosi: {min(punkty)}')
# print(f'Wartośc maksymalna wynosi: {max(punkty)}')
# a = float(input("Podaj wybraną liczbę z listy: "))
# if a in punkty:
#     print(punkty.index(a))
# else:
#     print("Liczba nie występuje na liście")