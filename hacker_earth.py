'''
s=input()
sum1=0
a=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
for i in s:
    if i in a:
        b=(a.index(i))+1
        sum1=sum1+b
print(sum1)
'''
'''
a1 = 0
a2 = 1000
lst=[]

print("prime numbers between {0} and {1} are :".format(a1 , a2))
for num in range(a1, a2+1):
    if num > 1:
        isDivisible = False
        for index in range(2, num):
            if num % index == 0:
                 isDivisible = True
        if not isDivisible:
            lst.append(num)
print(lst)
f=[]
s=[]
m=[]
for k in range(len(lst)-1):
    if abs(lst[k]-lst[k+1])==2:
        m.append(lst[k])
    
        m.append(lst[k+1])
      
        s.append(m)
print(s)
     
        for h in s:
            if len(h)==2:
                f.append(h)
    print("\nTwim Prime list : \n")
    print(f)
'''
'''
import emojis
import emoji
import tkinter as tk
online_root=tk.Tk()
b=emojis.encode('\U0001f600')
print(b)
sen_text=tk.Text(online_root,font="arial 11",height=1,width=30)
sen_text.place(x=95,y=190)
sen_text.insert(tk.INSERT,"U0001f600")
url=tk.Label(online_root,text=b,font="arial 11")
url.place(x=17,y=20)
online_root.mainloop()
'''
'''
s=input()
r=s[::-1]
print(r)
if s==r:
    print("yes")
else:
    print("no")    
'''  
n=int(input())

for i in range(n):
    h,m,eh,em=map(int,input().split())
    a=h*60+m
    b=eh*60+em
    c=abs(a-b)
    print("{} {}".format(c//60,c%60))

  
