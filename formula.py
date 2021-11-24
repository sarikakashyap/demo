from math import *

class formula:
    def __init__(self):
        print("Press A for (a+b)^2")
        print("Press B for (a-b)^2")
        print("Press C for (a)^2-(b)^2")
        print("Press E for (a+b)^3")
        print("Press F for (a-b)^3")
        print("Press G for (a-b-c)^2")
        print("Press H for (a+b+c)^2")
        print("Press I for (a-b-c)^3")
        print("Press J for (a+b+c)^3")
       
        

    def insert1(self,a,b):
        self.no=a
        no=int(input("enter the value of a: "))
        self.no2=b
        no2=int(input("enter the value of b: "))
    def A(self):
        insert1(no,no2)
        c=no+no2
        print("(a+b)^2="+pow(c,2))
#ch1=input(("Enter option: "))        
#while ch1!="n":
f=formula()
f.insert1()
ch2=input(("Enter optionto perform: "))
if ch2=="A" :
    f.A()
