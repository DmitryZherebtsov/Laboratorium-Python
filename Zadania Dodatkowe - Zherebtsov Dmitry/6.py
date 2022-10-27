a = int(input("Napisz pierwszą liczbę: "))
b = int(input("Napisz drugą liczbę: "))
print(" Wybierz metodę, którą chcesz obliczyć [ +, -, *, /, %]: ")
znak = str(input(" "))
if znak == "+":
    print("Wynik: ", a + b)
elif znak == "-":
    print("Wynik: ", a - b)
elif znak == "*":
    print("Wynik: ", a * b)
elif znak == "/":
    print("Wynik: ", a / b)
elif znak == "%":
    print("Wynik: ", a % b)
else:
    print("Error: Spróbuj ponownie")

