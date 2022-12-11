
def find_func(wartość, lista):
    length = len(lista)
    i = 0
    indeksy = []
    for i in range(length):
        if wartość == lista[i]:
            # print("Wartość ", wartość, " występuje w liście pod indexem", i)
            indeksy.append(i)
    print("Indeksy: ", indeksy)


# lista = [1, 2, 3, 4, 5, 5, 5]

find_func(5, [1,2,3,6,5,3,5,8,7,5,5])


# def find(wartosc, lista):
#     x = 0
#     indeksy = []
#     for i in lista:
#         if i == wartosc:
#             indeksy.append(x)
#         x += 1
#     return indeksy
#
#
# E = find(3, [8, 9, 5, 4])
# print(E)

