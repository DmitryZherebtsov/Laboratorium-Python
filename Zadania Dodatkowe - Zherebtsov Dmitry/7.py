x = str(input("Napisz literę: "))
if x.islower():
    print("Wynik: ", str.capitalize(x))
elif x.isupper():
    print("Wynik: ", str.lower(x))
else:
    print("Spróbuj ponownie napisać literę")