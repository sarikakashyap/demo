import tkinter as tk
import os
root = tk.Tk()

root.configure(bg="pink")

root.state("zoom")
root.iconbitmap("C:/Users/Nakul/Desktop/python/Whatsapp.ico")
root.title("HOME")
global loginbutt
global signbut
global sy

global name1,confpass1,pass1
sy=tk.Label(root,text="-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
sy.config(justify="center",bg="pink",fg="pink")
sy.grid(row=1 , padx=20,pady=20)

def home():
    
    sy.grid(row=0,columnspan=2)
    def remove():
        loginbutt.destroy()
        signbut.destroy()
        
    loginbutt=tk.Button(root,text="LOGIN ",height=3,width=18,font="Arial 25 bold",command=lambda :[root.destroy(),login()])
    loginbutt.grid(row=1,column=0,pady=250)

    
    signbut=tk.Button(root,text="SIGNUP",height=3,width=18,font="Arial 25 bold",command=lambda :[remove(),signup()])
    signbut.grid(row=1,column=1,pady=250,padx=50)
    root.mainloop()
def remove2():
        rootlogin.destroy()
        
def login():
    rootlogin=tk.Tk()
    rootlogin.configure(bg="pink")
    rootlogin.state("zoom")
    
   
       
 
    sym=tk.Label(rootlogin,text="---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
    sym.config(justify="center",bg="pink",fg="pink")
    sym.grid(row=1 , padx=20,pady=15)
  
    login=tk.Label(rootlogin,text="LOGIN FORM",font="Arial 40 bold ")
    login.config(bg="pink",justify="center")
    login.grid(row=2 , padx=20,pady=15)

    name=tk.Label(rootlogin,text="USER NAME",font="Arial 30 ")
    name.config(bg="pink",anchor="center")
    name.grid(row=3,pady=15)

    nentry=tk.Entry(rootlogin,font="Arial 15 ")
    #nentry.insert(0,"Login username")
    #nentry.configure(state="normal")
    nentry.grid(row=4,padx=20,pady=15,ipadx=50,ipady=5)
    
        
    '''sym.destroy()
    login.destroy()
    name.destroy()
     
    password.destroy()
    sub.destroy()
    can.destroy()

    nentry.destroy()
    passentry.destroy()
    cpassentry.destroy()
    cpassword.destroy()
        
    subhome2.destroy()
    #confirm.destroy()'''
    
        
    def fun():
        name1=nentry.get()
        pass1=passentry.get()
        confpass1=cpassentry.get()
##        confirm=tk.Label(root,text="Submitted")
##        confirm.grid(row=11)

        path1="C:/Users/Nakul/Desktop/python/signup/"
        #print(name1=nentry.get())
        namefile=os.listdir(path1)
        print(namefile)
        ext=name1+".txt"
        
        if ext in namefile:
            print("ok")
            passcheck=open(path1+ext,"r")
            passcheck1= passcheck.read()
            if passcheck1==pass1:
                print("password matches ")
            else:
                print("wrong passwd")
            
            
            path="C:/Users/Nakul/Desktop/python"

            file=open(path+"/login.txt","a")
            
            print("UserName \t Password \t Confirm Password")
           
            
            uname=file.write("UserName:"+name1+"\t\t")
            print(uname)
            print(file.write("Password:"+pass1+"\t\t"))
            print(file.write("Confirm Password:"+confpass1+"\n"))
            file.write("----------------------------------------------------------------------------------------------------------------\n")
        else:
            print("no")


    def clear():
        nentry.delete(0,'end')
        passentry.delete(0,'end')
        cpassentry.delete(0,'end')
        

        
    password=tk.Label(rootlogin,text="PASSWORD",font="Arial 30 ")
    password.config(bg="pink",anchor="center")
    password.grid(row=5,pady=15)

    passentry=tk.Entry(rootlogin,font="Arial 15 ")
    #passentry.insert(0,"Login Password")
    passentry.config(show="*")
    passentry.grid(row=6,padx=20,pady=15,ipadx=50,ipady=5)

    cpassword=tk.Label(rootlogin,text="CONFIRM PASSWORD",font="Arial 20 ")
    cpassword.config(bg="pink",anchor="center")
    cpassword.grid(row=7,pady=15)

    cpassentry=tk.Entry(rootlogin,font="Arial 15 ")
    #cpassentry.insert(0,"Enter confirm password")
    cpassentry.config(show="*")
    cpassentry.grid(row=8,padx=20,pady=15,ipadx=50,ipady=5)


    sub=tk.Button(rootlogin,text="SUBMIT",height=2,width=15,command=lambda:[fun(),clear()])
    sub.grid(row=9,padx=10,pady=15)

    can=tk.Button(rootlogin,text="CANCEL",height=2,width=15)
    can.grid(row=10,padx=10)
    
    subhome2=tk.Button(rootlogin,text="HOME",height=2,width=15,command=lambda:[remove2(),home()])
    subhome2.grid(row=0,padx=10,pady=15)

def signup():
    subhome=tk.Button(root,text="HOME",height=2,width=15,command=lambda:[remove1(),home()])
    subhome.grid(row=0,padx=10,pady=20)
   
        
        
    sym=tk.Label(root,text="---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
    sym.config(justify="center",fg="pink",bg="pink")
    sym.grid(row=1 , padx=20,pady=10)
    def remove1():
        sym.destroy()
        sign.destroy()
        name.destroy()
       
        password.destroy()
        sub.destroy()
        can.destroy()

        nentry.destroy()
        passentry.destroy()
        
       
        subhome.destroy()

    def fun2():
        uname=nentry.get()
        passwd=passentry.get()
        
        path="C:/Users/Nakul/Desktop/python/signup/"
        file=open(path+uname+".txt","w")
        file.write(passwd)

    def clear1():
        nentry.delete(0,'end')
        passentry.delete(0,'end')
        
    sign=tk.Label(root,text="SIGNUP FORM",font="Arial 30 bold ")
    sign.config(bg="pink",justify="center")
    sign.grid(row=2 , padx=20,pady=10)

    name=tk.Label(root,text="USER NAME",font="Arial 20 ")
    name.config(bg="pink",anchor="center")
    name.grid(row=3,pady=20)

    nentry=tk.Entry(root,font="Arial 15 ")
    #nentry.insert(0,"Enter username")
    #nentry.configure(state="normal")
    nentry.grid(row=4,padx=20,pady=20,ipadx=50,ipady=5)

    password=tk.Label(root,text="PASSWORD",font="Arial 20 ")
    password.config(bg="pink",anchor="center")
    password.grid(row=5,pady=20)

    passentry=tk.Entry(root,font="Arial 15 ")
    #passentry.insert(0,"Enter password")
    passentry.config(show="*")
    passentry.grid(row=6,padx=20,pady=20,ipadx=50,ipady=5)

    
    sub=tk.Button(root,text="SUBMIT",height=2,width=15,command=lambda:[fun2(),clear1()])
    sub.grid(row=9,padx=10,pady=20)

    can=tk.Button(root,text="CANCEL",height=2,width=15)
    can.grid(row=10,padx=10)

home()


