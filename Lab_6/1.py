
def func_1(imię="NoName", wiek=20):       #imię="NoName" i wiek=20 - to jest wartość jak default2
    ''' Funkcja wypisująca imię i wiek '''
    print(imię, " ", wiek)

a = input("Podaj imię: ")
b = int(input("Podaj wiek: "))
# func_1("Dmitry", 17)
func_1(a, b)

func_1(wiek=19, imię="Max")
func_1(imię="Max") #Max   20
# print(func_1.__doc__)
# print(help(func_1))
