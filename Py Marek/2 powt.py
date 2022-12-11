a = False
print(not a)

#####

py = "Py"
thon = "thon!"
print(py + thon)

#####

lista = [12, 13.2, False, 'Hey', None]
lista_wynik = []
l = len(lista)
for i in range(l):
    g = lista[i]
    k = type(g)
    lista_wynik.append(k)
    i += 1
print(lista_wynik)

#####

smth = (90, "Ninety", 90.0, True)
print(smth[1][0:4])


