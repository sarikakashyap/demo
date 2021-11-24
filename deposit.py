import os

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

'''def deposit():
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
         #sum2=file_read[2]
         
         #file_open=open(path+file2,"w")
         #file_open.writelines(sum2)
         #file_open.close()
    else:
         print("account not exist")'''
b=input("enter : ")        
if b=="d":
    moneytransfer() 