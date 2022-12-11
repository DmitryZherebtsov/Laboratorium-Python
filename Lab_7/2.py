import numpy as np

macierz = np.random.randint(low=0, high=25, size=(5,5))
print(macierz)


print(" Minimalna: ", macierz.min())
print(" Maxymalna: ", macierz.max())



print(" Minimalna wartość wirsza 0: ", macierz.min(axis = 1))
print(" Maxymalna wartość wirsza 0: ", macierz.max(axis = 0))

#axis = 1 - wierszy
#axis = 0 - kolumny

#
# macierz = np.random.randint(low = 0 , high = 25, size = (5, 5))
# print(macierz)
# print()
# print("Wartosc minimalna: ", macierz.min())
# print("Wartosc maksymalna: ", macierz.max())
# print("Wartosci minimalne wiersza: ", macierz.min(axis = 1))
# print("Wartosci maksymalne wiersza: ", macierz.max(axis = 0))
# print("Suma poszczegolnych wierszy wynosi: ", macierz.sum(axis = 1))