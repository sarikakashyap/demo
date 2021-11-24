'''# i=1
# while i<10:
#     print(i)
#     if(i==5):
#         break
#     i+=1
i=1
# while i<10:
#     i+=1
    
    
#     if(i==5):
#         continue
#     print(i)  
i=1
# while i<5:
#      print(i)
#      i+=1 
# else:
#     print("i is no longer valid")
       

#  while(1):
#    username=str(input("enter name="))

# for x in "apple":
#     print(x , end=" $")
# for x in range(2,6):
#     print(x)
# for x in range (1,10,2):
#     print(x)
# a=["a","b","c"]
# b=["x","y","z"]
# for c in a:
#     for d in   b:
#         print(c,d)
#list
list=["apple","mango",1,"cat","dog","hut"]
list2=["A","B","C","D","E"]
print(list)
#Access
print(list[1])
#negative index
print(list[-1])
#ranre indexing
print(list[1:4:2])
#range to end of list with slicling , [start:end:slicing]
print(list[1::2])
#changing item in a list
list[3]="CAT"
print(list)
#using loop in list
for i in list:
    #print(i)
    print(i,end=",")
list.append("FRUIT")
print(list)    
list.append(list2)
print(list)
#insert item at particulat place
list2.insert(2,"apple")
print(list2)
'''

a=5
for x in range(1,11):
    #print(a+"x"+x+"="+int(a*x))
    print("{}x{}={}".format(a,x,a*x))
    '''
month31= ["january" ,"march","may","july","august","october","december"]
month30=["april","june","september","november"]
month="february"
no=int(int(input("enter month days")))
if no==31:
    print(month31)
elif no==30:
    print(month30)
elif (no==28 or no==29):
    print(month)
else:
    print("enter correct no ")     '''       