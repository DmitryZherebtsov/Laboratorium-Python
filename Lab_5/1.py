######
values = [10, 20, 30]
keys = ['Ten ', 'Twenty ', 'Thirty ']
R = dict(zip(keys, values))
# print(R)
print(list(zip(keys, values)))

x= len(keys)
for i in range(x):
    R[keys[i]] = values[i]
print(R)

######

D = dict(Fourty = 40, Fifty=50, Sixty = 60)
D1 = R.copy()
D1.update(D)
print(D1)


######
#
# D2 = dict(Thirty = 30, Fourty = 40, Fifty= 50)
# D3 = dict(Sixty = 60, Seventy = 70, Eighty= 80)
# # D4 = D2.copy(), D3.copy()
#
# D4 = dict(zip())
#
# print(D4)
