
import math
from math import  *



def add1(a,b):
        return a+b
def sub(a,b):
        return a-b
def mul(a,b):
        return a*b
def div(a,b):
        return a/b
def rem(a,b):
        return a%b
def sqrt1(a):
        print("sqrare root  of number one is : {} ".format(sqrt(a)))
def power(a,b):
        print("Number {} having Power {} :{}".format(a,b,pow(a,b)))
def log1(a):
        print("Log Base 10  of number one is : {} ".format(log10(a)))
def Log(a):
        print("Natural Log Base e of number one is : {} ".format(log(a)))
def fac(a):
        print("factorial of number  is : {} ".format(factorial(a)))
def angle(a,c):
        if(c=="S"):
                print("Sin angle in degrees of the value is {}".format(degrees(asin(a))))
        elif(c=="T"):
                print("Tan angle in degrees of the value is {}".format(degrees(atan(a))))
        elif(c=="C"):
                print("Cos angle in degrees of the value is {}".format(degrees(acos(a))))        
                
        else:
                print("plz enter correct option :  ")
def value(a,dr,c):
        if dr=="R":
                if(c=="S"):
                        print("Sin angle value is {}".format(sin(a)))
                elif(c=="T"):
                        print("Tan angle  value is {}".format(tan(a)))
                elif(c=="C"):
                        print("Cos angle  value is {}".format(cos(a)))       
                
                else:
                        print("plz enter correct option :  ")
        if dr=="D":
                r=math.radians(a)
                if(c=="S"):
                        print("Sin angle value is {}".format(sin(r)))
                elif(c=="T"):
                        print("Tan angle  value is {}".format(tan(r)))
                elif(c=="C"):
                        print("Cos angle  value is {}".format(cos(r)))       
                
                else:
                        print("plz enter correct option :  ")        

        
        
print("You are in Calculator !!! Do you want to contonue")    
print("Enter n to exit")
print("Enter y to continue")
ch1=input("enter choice:")
while ch1!="n":
    
    print("-----------------------------------------")
    print("To perform the Operation under ** block ...First Enter Option")

    print("Press + for addition")
    print("Press - for substraction")
    print("Press * for Multiplication")
    print("Press / for Division")
    print("Press % for Remainder")
    print("***************************************************************")
    print("Press s for Square root of no")
    print("Press p for  Power Function")
    print("Press L for  Natural Log")
    print("Press l for   Log Base 10")
    print("Press f for Factorial of no")
    print("Press a To find the angle")
    print("Press V To find the value of given angel")

    
    print("***************************************************************")

    print("-----------------------------------------")
    print()
    print("Enter n to exit Or To continue press Y or any key")    
    ch=input("enter choice:")
    if(ch=="n"):
       break
    elif (ch=="p"):
            nop=int(input("Enter no: "))
            po=int(input("Enter power: "))
            power(nop,po)
            continue
    elif (ch=="s"):
            nop=int(input("Enter no: "))
            
            sqrt1(nop)
            continue
    elif (ch=="L"):
            nop=int(input("Enter no: "))
            
            Log(nop)
            continue
    elif (ch=="l"):
            nop=int(input("Enter no: "))
            log1(nop)
            continue
    elif (ch=="f"):
            nop=int(input("Enter no: "))
            fac(nop)
            continue
    elif (ch=="a"):
            nop=float(input("Enter value: "))
            print("###########################################")
            print("press T to find the  Tan angel")
            print("press S to find the  Sin angel")
            print("press C to find the  Cos angel")
            
            print("###########################################")
            ch1=input("choose Option")
            angle(nop,ch1)
            continue
    elif (ch=="V"):
            print("----------------------------------------------------------------------")

            print("Press D to enter angel in Degrees and Press R to enter angel in radian:")
            print("----------------------------------------------------------------------")
            DR=input("press Option : ")
            if DR=="R":
                    nop=float(input("Enter Angel in radian: "))
            if DR=="D":
                    nop=float(input("Enter Angel in Degrees: "))
                    
            print("###########################################")
            print("press T to find the  Tan angel Value")
            print("press S to find the  Sin angel Value")
            print("press C to find the  Cos angel Value")
            
            print("###########################################")
            ch1=input("choose Option: ")
            value(nop,DR,ch1)
            continue  
        
    no1=int(input("Enter first no: "))
    no2=int(input("Enter Second no: "))
    ch=input("enter Operation choice:")
    if(ch== "+"):
        print("Addition of number is : {}".format(add1(no1,no2)))
    elif(ch== "-"):
        print("Subtraction of number is : {}".format(sub(no1,no2)))    
            
    elif(ch== "*"):
        print("Multiplication of number is : {}".format(mul(no1,no2)))
    
    
    elif(ch== "/"):
        print("Division  of number is : {}".format(div(no1,no2)))

    elif(ch== "%"):
        print("Remainder of number is : {}".format(rem(no1,no2)))
    elif(ch== "s"):
        (sqrt1(no1,no2))
    else:
        print("Please Press correct Operation")
    
