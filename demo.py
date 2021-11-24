##x=lambda a :a+10
##print(x(62))
##
##y=lambda a,b :a+b
##print(y(12,12))
##
##z= lambda a,b,c,d,:(a+b)*(c+d)
##print(z(1,2,3,4))


##def fun(n):
##    return lambda a:a*n
##a=(fun(5))
##print(a(2))
##


# Class And Objects

##class First:
##    def a(self,b):
##       print("hello "+b)
##f=First()
##f.a("sarika")

##class second:
##    x=20
##s=second()
##print(s.x)
##
##class first:
##    def __init__(self,a,b):
##        print("this is in it function :{}, {}".format(a,b))
##f=first(1,2)        
##


class abc:
    def __init__(sarika,a,b):
        sarika.first=a
        sarika.second=b
    def fun(alka):
        print("function call: "+alka.first)
        print("Function call second parameter "+alka.second)

ob=abc("nandini","Moni")
ob.first="Parul"
del ob.second
del ob
ob.fun()













































































