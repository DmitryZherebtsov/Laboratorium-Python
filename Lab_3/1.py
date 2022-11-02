x = int(input("Wpisz 1 wartość: "))
y = int(input("Wpisz 2 wartość: "))

if x > y:
    x, y = x, y

while x <= y:
    print(x)
    x += 1

