#Pirwsza wersja
n = int(input())
for i in range(n+1):
    print("" * (n-i)+"*"*i)

#Druga wersja
n = int(input())
for i in range(n+1):
    print(" " * (n-i)+"* "*i)


