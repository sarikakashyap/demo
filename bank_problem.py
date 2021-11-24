import os
print("press 'c' for Current account")
print("press 's' for show account")
print("press 'd' for deposit account")
print("press 'm' for money transfer")
print("press del for delete account")
opt=input("Enter option:")

def currentacc():
    name=str(input("enter user name: "))
    age=int(input("Entre Age: "))
    amount=int(input("Enter Amount:"))
    accno=str(input("Enter Account no: "))
    createfile=("{}{}".format(accno,".txt"))
    typeacc=str(input("Enter Type of account,(saving or current):"))
    path="D:/data_bankManagement/"
    file=open(path+createfile,"a")
    file.write("Name:{}\nAge{}\n{}\nType of Account: {}".format(name,age,amount,typeacc))
def deposit():
    path="D:/data_bankManagement/"
    acc=input("Enter Account no:")
    file1=os.listdir(path)
    file2=acc+".txt"
    if file2 in file1:
         file_open=open(path+file2,"r")
         file_read=file_open.readlines()
         a=file_read[2]
         
         print(" Account Exist")
         print("balance:"+a)
         dep=int(input(("Enter deposit Amount:")))
         sum=dep+int(a)
         sum2=str(sum)
         print("After deposit balance is :{}".format(sum))
         f = open(path+file2, "rt")
         data = f.read()
         data = data.replace(a, sum2+"\n")
         f.close()
         f = open(path+file2, "wt")
         f.write(data +"\n")
         f.close()
    else:
         print("account not exist")
    
def savingacc():
    path="D:/data_bankManagement/"
    acc=str(input("Enter Account no:"))
    file1=os.listdir(path)
   # print(file1)
    file2=acc+".txt"
    if file2 in file1:
        print("yes")
        file=open(path+acc+".txt","r")
        check=file.read()
        print(check)
    else :
        print("Invalid account")
def deleteacc():
    path="D:/data_bankManagement/"
    acc=str(input("enter Account which you want to delete : "))
    file1=acc+".txt"
    file2= os.listdir(path)
    print(file2)
    if file1 in file2:
        print("yes")
        os.remove(path+file1)
        
        print("deleted")
    else:
        print("file not exist")    

def moneytransfer():
    path="D:/data_bankManagement/"
    send=str(input("enter sender account no: "))
    rec=str(input("enter Receiver account no: "))
    sendfile=send+".txt"
    recfile=rec+".txt"
    file = os.listdir(path)
    if sendfile in file and recfile in file:
        print("yes")
        file=open(path+sendfile,"r")
        file_read= file.readlines()
        amount=file_read[2]

        file_rec=open(path+recfile,"r")
        file_read1= file_rec.readlines()
        amount_rec=file_read1[2]


        enter_amount=int(input("Enter Amount : "))
        if enter_amount<int(amount):
            print("true")
            diff=int(amount)-enter_amount
            sum=int(amount_rec)+enter_amount

            f=open(path+sendfile,"rt")
            recf=open(path+recfile,"rt")
            record_sender=f.read()
            record_receiver=recf.read()

            record_sender=record_sender.replace(amount,str(diff)+"\n")
            record_receiver=record_receiver.replace(amount_rec,str(sum)+"\n")
            f.close()
            f=open(path+sendfile,"wt")
            f.write(record_sender+"\n")
            f.close()

            f1=open(path+recfile,"wt")
            f1.write(record_receiver+"\n")

            f1.close()
        else:
            print("balance is not sufficient")    
    elif sendfile not in file :
        print("sender account not exist")    
    elif recfile not in file :
        print("Receiver account not exist")     
    else:
        print("both are invalid account")               







if opt=="s":
    savingacc()
elif opt=="c":
    currentacc()
elif opt=="d":
    deposit()
elif opt=="del":
    deleteacc()    
elif opt=="m":
    moneytransfer()
else:
    print("please select correct option")
