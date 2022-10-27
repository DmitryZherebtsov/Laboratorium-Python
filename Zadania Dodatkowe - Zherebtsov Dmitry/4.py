
x = int(input("Napisz wartość funkcji x: "))
y = int(input("Napisz wartość funkcji y: "))
z = int(input("Napisz wartość funkcji z: "))
list = [x, y, z]
length = len(list)
for i in range(0, length-1):
    for j in range(0, length-1-i):
        if list[j] > list[j+1]:
            list[j], list[j+1] = list[j+1], list[j]
print(list)

