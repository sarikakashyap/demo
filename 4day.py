'''#TUPLE

a=("A","B","C")
q="A","B","C"
b=list(a)
b[1]="b"
z=tuple(b)
print(z)
print(type(a))
print(type(q))'''
'''
#set

a={"a","b","c","d","e"}
print("set"+str(a))
b={1,2,3,4}
c=a.union(b)#it will merge two sets
a.update(b)#it will update the set a
print(a)
print(c)'''


dic={"fruit":"apple","veg":"potato","nonveg":"egg"}
print(dic["fruit"])
for x in dic:
    print("key="+str(x))
print("---------------------------------")
for y in dic:
    print(dic[y])
print("---------------------------------")    
for z in dic.values():
    print(z)
print("---------------------------------")    
for a,b in dic.items():
    print(a,b)            