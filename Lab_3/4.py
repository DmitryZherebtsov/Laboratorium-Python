x = int(input("Wpisz 1 wartość: "))
y = int(input("Wpisz 2 wartość: "))

if x > y:
    x, y = y, x


while x <= y:
    if x % 2 == 1:
        x = x + 1
        continue
    print(x)
    x = x + 1
