
#Welcome Message
Val=input("Enter your name: ")
print(f'Hello ,{Val}!')
#print("Hello "+Val+"!")


print("---------------------------------------------------------------------")

#Pay calculation
hours_val=int(input("Enter Hours: "))
rate_val=float(input("Enter Rate: "))
pay=hours_val*rate_val
print("Pay: ${}".format(pay))
print("---------------------------------------------------------------------")

#type and value check of expression
width=17
height=12.0
result= width//2         #first Expression
result1=width /2.0       #second expression
result2=height /3        #third expression
result3=1+2 *5           #fourth expression
print("Value: {}  and  type: {} of first expression ".format(result,type(result)))
print("Value: {}  and  type: {} of second expression ".format(result1,type(result1)))
print("Value: {}  and  type: {} of third expression ".format(result2,type(result2)))
print("Value: {}  and  type: {} of fourth expression ".format(result3,type(result3)))

print("---------------------------------------------------------------------")

#Convert Celsius temperature into Fahrenheit

celsius=float(input("Enter Celsius Temperature: "))
fahrenheit=(celsius * 1.8 )+32
print("Temperature in fahrenheit: {}".format(fahrenheit))