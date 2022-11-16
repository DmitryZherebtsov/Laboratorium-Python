zwierzeta = []
x = 5

for i in range(x):
    a = input("Podaj nazwe zwierzecia: ")
    zwierzeta.append(a)

zwierzeta.sort()

print(zwierzeta[0])
print(zwierzeta[-3:])
print(len(zwierzeta))