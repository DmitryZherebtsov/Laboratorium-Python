# type()
def znaki(string):
    dict1 = {}
    for i in string:
        dict1[i] = dict1.get(i, 0) + 1
   #     if i in dict1:
    #       dict1[i] = dict1[i] + 1
     #   else:
      #      dict1[i] = 1
    return dict1


slownik = znaki('znaki napisu')
print("NOT sorted", slownik)

lista_kluczy = sorted(slownik)

print("Sorted: ")
for i in sorted(znaki('znaki napisu')):
    print(i, slownik.get(i))

