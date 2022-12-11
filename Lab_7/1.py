# Zadamie 1
import numpy as np

# arr = [128, 64, 32, 16, 8, 4, 2, 1]
# arr = []
# for i in range(7, -1, -1):
#     arr.append(2**i)

arr=[2**i for i in range (7, -1, -1)]
print(arr)

wagi = np.array(arr)
print(wagi)

liczba_bin = np.random.randint(low=0, high=2, size=8)
print(liczba_bin)

dziesietny = wagi*liczba_bin
print(dziesietny)

suma = dziesietny.sum()
print(suma)


# import numpy as np
# arr=[2**i for i in range(7,-1,-1)]
# print(arr)
# wagi= np.array(arr)
# print(wagi)
# liczba_bin= np.random.randint(low=0, high=2, size=8);
# print({liczba_bin})
# dziesietny= wagi*liczba_bin
# print(dziesietny)
# suma= dziesietny.sum()
# print(suma)

