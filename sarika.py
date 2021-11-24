def fun(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        #print("resursion")
        return fun(n-1)+fun(n-2)
        

import sarika
#from fibonicay import fun
print(sarika.fun(7))