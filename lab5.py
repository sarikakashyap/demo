
#1
total=0
count=0

while(True):
        num=input("Enter a number:")
        if num=="done" or num =="Done":
            break        
        try:
            num2=int(num)               
            total= total+num2
            count= count+1
                        
        except:
            print("Invalid number entered!")   
            continue   

avg=total/count
print(f"Total: {total}")    
print(f"Count: {count}")
print(f"Average: {avg}")    

'''
#2
total=0
count=0
min_num=None
max_num=None
while(True):
    
        num=input("Enter a number:")
        if num=="done" or num =="Done":
            break        
        try:
            num2=int(num)               
            total= total+num2
            count= count+1
            if min_num is None :
                min_num=num2
            if max_num is None:
                max_num=num2    
            min_num=min(min_num,num2)
            max_num=max(max_num,num2)
            
        except:
            print("Invalid number entered!")   
            continue 
        
avg=total/count
print(f"Total: {total}")    
print(f"Count: {count}")
print(f"Average: {avg}")
print(f"Lowest: {min_num}")
print(f"Highest: {max_num}")
'''