
print(" ****** Odpowiedz Tak lub Nie ****** ")
a_1 = str(input("Czy pada deszcz? Twoja odpowiedź: "))
a_2 = str(input("Czy jest autobus na przystanku? Twoja odpowiedź: "))

if a_1 == "Tak" and a_2 == "Tak":
    print(' Weź parasol. Dostaniesz się na uczelnie!')
elif a_1 == "Tak" and a_2 == "Nie":
    print('Nie dostaniesz się na uczelnię!')
elif a_1 == "Nie" and a_2 == "Tak":
    print('Dostaniesz się na uczelnie!')
elif a_1 == "Nie" and a_2 == "Nie":
    print('Nie dostaniesz się na uczelnię!')
else:
    print("Spróbuj ponownie")

end = str(input())
