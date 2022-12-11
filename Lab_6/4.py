def func_4(**kwargs):
    if 'end' in kwargs:
        endfunc_4 = kwargs['end']
    else:
        endfunc_4 = '\n'

    endfunc_4 = kwargs.get('end', '\n')
    for key, value in kwargs.items():
        print(key, value, end = endfunc_4)
        # print(key, value, end=' ') zamiast '\n'
# func_4(par1 = 1, par2 = 2, par3 = 3, par4 = 4, par5 = 5, end = "END")
func_4(par1 = 1, par2 = 2, par3 = 3, par4 = 4, par5 = 5)


# def f1(**kwargs):
#     #if 'end' in kwargs:
#     #    endF1 = kwargs['end']
#     #else:
#     #    endF1 = "\n"
#     endF1 = kwargs.get('end', '\n')
#     for key, value in kwargs.items():
#         print(key, value,end=endF1)
# f1(par1=1, par2=2, par3=3, par4=4, par5=5, end="dfdsg")