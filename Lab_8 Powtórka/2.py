
dict1 = {'data1': 10, 'data2': -4, 'data3': 2}
dict2 = {'data1': 20, 'data2': -14, 'data3': 4}

def sum_of_values(s1):
    j = 0
    for i in s1.values():
        j = j + i
    return(j)
a = sum_of_values(dict1)
print(a)
b = sum_of_values(dict2)
print(b)

# dict1 = {'data1':10, 'data2':-4, 'data3':2}
# dict2 = {'asfsaf':1, 'asfasfasdfgasd':-5, 'sdgdsjghdsjakajskghd':10000}
# def sum_of_values(s1):
#     j = 0
#     for i in s1.values():
#         j = j + i
#     return(j)
# b= sum_of_values(dict1)
# c = sum_of_values(dict2)
# print(b)
# print(c)