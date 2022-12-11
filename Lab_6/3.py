'''Zadanie 3 '''

# def funkcja_3(*args):
#     print(type(args))
#     print(args)
#     for i in args:
#         print(i, type(i))
#
# funkcja_3(30, 88.8, "Str", True, [3, 4, 5], False)
# funkcja_3()
# funkcja_3(44, True, 3.2, "Hey")


# max(30, 43, 56, 69)

# def max_4(*args):
#     if len(args) == 0:
#         return None
#     i = args[0]
#     for j in args[1:]:
#         if j > i:
#             i = j
#     return i
#
# res = max(30, 44, 59, 75)
# print("Wartość maksymalną: ", res)
# print(max_4)



def max(*args):
    if len(args) == 0:
        return None
    m = args[0]
    for i in args[1:]:
        if i > m:
            m = i
    return m
wynik = max(31,4,19,23)
print(wynik)
print(max("Zh. Dmitry", "Ivan", "Max"))