import random
# punkty = []

# for i in range(15):
#     p = random.uniform(0, 50)
#     p = round(p,2)
#     # punkty.append(round(p))
#     punkty.append(p)

punkty = [round(random.uniform(0, 50),2) for a in range(15)]
print(punkty)
print(f'Minimalne: {min(punkty)}')
print(f'Maxymalnie: {max(punkty)}')

# for punkty in range(1, 15):
