from math import *

class formula:
    def msg(self):
        print("Press A for (a+b)^2")
        print("Press B for (a-b)^2")
        print("Press C for (a)^2-(b)^2")
        print("Press E for (a+b)^3")
        print("Press F for (a-b)^3")
        print("Press G for (a-b-c)^2")
        print("Press H for (a+b+c)^2")
        print("Press I for (a-b-c)^3")
        print("Press J for (a+b+c)^3")
    def A(self):
        no=int(input("enter the value of a: "))
        no2=int(input("enter the value of b: "))
        c=no+no2
        print("(a+b)^2={}".format(pow(c,2)))
    def B(self):
        no=int(input("enter the value of a: "))
        no2=int(input("enter the value of b: "))
        c=no-no2
        print("(a-b)^2={}".format(pow(c,2)))
    def C(self):
        no=int(input("enter the value of a: "))
        no2=int(input("enter the value of b: "))
        c=pow(no,2)+pow(no2,2)
        print("(a+b)^2={}".format(c))
    def E(self):
        no=int(input("enter the value of a: "))
        no2=int(input("enter the value of b: "))
        c=no+no2
        print("(a+b)^3={}".format(pow(c,3)))
    def F(self):
        no=int(input("enter the value of a: "))
        no2=int(input("enter the value of b: "))
        c=no-no2
        print("(a-b)^3={}".format(pow(c,3)))
    def G(self):
        no=int(input("enter the value of a: "))
        no2=int(input("enter the value of b: "))
        no3=int(input("enter the value of c: "))
        c=no-no2-no3
        print("(a-b-c)^2={}".format(pow(c,2)))
    def H(self):
        no=int(input("enter the value of a: "))
        no2=int(input("enter the value of b: "))
        no3=int(input("enter the value of c: "))
        c=no+no2+no3
        print("(a+b+c)^2={}".format(pow(c,2)))
    def I(self):
        no=int(input("enter the value of a: "))
        no2=int(input("enter the value of b: "))
        no3=int(input("enter the value of c: "))
        c=no-no2-no3
        print("(a-b-c)^3={}".format(pow(c,3)))
    def J(self):
        no=int(input("enter the value of a: "))
        no2=int(input("enter the value of b: "))
        no3=int(input("enter the value of c: "))
        c=no+no2+no3
        print("(a+b+c)^3={}".format(pow(c,3)))    




f=formula()
f.msg()
ch1=input("Enter option if you want to continue: ")    
while ch1!="n":
    ch=input("Enter option: ")    

    if (ch=="n"):
        break
    elif (ch=="A"):
        f.A()
    elif ch=="B":
        f.B()
    elif ch=="C":
        f.C()
    elif ch=="D":
        f.D()
    elif ch=="E":
        f.E()
    elif ch=="F":
        f.F()
    elif ch=="G":
        f.G()
    elif ch=="H":
        f.H()
    elif ch=="I":
        f.I()
    elif ch=="J":
        f.J()     
    else:
        print("enter correct function")

        
