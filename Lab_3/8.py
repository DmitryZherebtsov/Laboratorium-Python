#gwiazdki
n = int(input())
i = 0
j = 0
gwiazdki = ""

for i in range(n):
    gwiazdki = gwiazdki + "*"
    i+=1
for j in range(n):
    print(gwiazdki)
    j += 1