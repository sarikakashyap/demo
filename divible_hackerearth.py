import math
n=int(input())
mid=int(n/2)
list1=[]
listf=[]
print("enter value:\n")
for i in range(0,n):
    c=int(input())
    list1.append(c)
for j in range(0,mid):
    while(list1[j]>=10):
        list1[j]/=10
    #print(int(list1[j]))
    b=listf.append(int(list1[j])) 
for k in range(mid,n):
    list1[k]=list1[k]%10
    listf.append(int(list1[k])) 
print(listf)  
print(len(listf))
for num in range(len(listf)):
    c=len(listf)-1
    while(c>=0):
        sum=int(listf[num])*pow(10,c)
        c=c-1
        print(sum)
        break;
       
