import math
a = int(input("Napisz wartość funkcji a: "))
b = int(input("Napisz wartość funkcji b: "))
c = int(input("Napisz wartość funkcji c: "))

d = b**2 - 4 * a * c
if d > 0:
    x1 = (-b+ math.sqrt(d)) / (2*a)
    x2 = (-b- math.sqrt(d)) / (2*a)
    print('Pierwiastki równania kwadratowego: \n x1 = ', x2, '\n x2 = ', x1)
elif a == 0 and b == 0 and c == 0:
        print("Spróbuj ponownie")
elif d == 0:
    x = -b / (2 * a)
    print("x = %.2f" % x)
else:
    print("Nie ma pierwiastków")
