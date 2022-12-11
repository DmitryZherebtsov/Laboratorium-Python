L1 = [1,2,3,4]
L2 = [4,3,2,2, 4]

def potęga(lista_1, lista_2):
    i = 0
    wynik = []
    if len(lista_1) != len(lista_2):
        print("Listy są różne")
        return wynik
    for i in range(len(lista_1)):
        x = lista_1[i]**lista_2[i]
        # print(lista_1[i]**lista_2[i])
        i += 0
        wynik.append(x)
    print("Lista z wynikami ", wynik)

potęga(L1, L2)





