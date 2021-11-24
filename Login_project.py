import tkinter as tk
import os
from tkinter import messagebox
global loginbutt
global signbut
global sy

global name1,confpass1,pass1


def home():
    root = tk.Tk()
    root.configure(bg="black")
    root.state("zoom")
    root.iconbitmap("C:/Users/Nakul/Desktop/python/Whatsapp.ico")
    root.title("HOME")
    sy=tk.Label(root,text="---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
    sy.config(justify="center",bg="black",fg="black")
    sy.grid(row=1 , padx=20,pady=150)
    
    sy.grid(row=0,columnspan=2)
    
        
    loginbutt=tk.Button(root,text="LOGIN ",height=3,width=10,font="Arial 12 bold",bg="orange" ,fg="black",command=lambda :[root.destroy(),login()])
    loginbutt.grid(row=1,column=0,pady=50)

    
    signbut=tk.Button(root,text="SIGNUP",height=3,width=10,font="Arial 12 bold",bg="orange" ,fg="black",command=lambda :[root.destroy(),signup()])
    signbut.grid(row=1,column=1)
    root.mainloop()
'''def remove2():
        rootlogin.destroy()'''
        
def login():
    rootlogin=tk.Tk()
    rootlogin.configure(bg="black")
    rootlogin.state("zoom") 
 
    #sym=tk.Label(rootlogin,text="---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
    #sym.config(justify="center",bg="black",fg="black")
    #sym.grid(row=1,columnspan=2 ,pady=15)
    
    subhome2=tk.Button(rootlogin,text="HOME",height=2,width=15,bg="orange" ,fg="black",command=lambda:[rootlogin.destroy(),home()])
    subhome2.grid(row=0,columnspan=2,pady=15)
  
    login=tk.Label(rootlogin,text="LOGIN FORM",font="Arial 14 bold ")
    login.config(bg="black",fg="white",justify="center")
    login.grid(row=2 ,columnspan=2,pady=15)

    name=tk.Label(rootlogin,text="USER NAME",font="Arial 12 ")
    name.config(bg="black",fg="white",anchor="center")
    name.grid(row=3,columnspan=2,pady=15)

    nentry=tk.Entry(rootlogin,font="Arial 12 ")
    #nentry.insert(0,"Login username")
    #nentry.configure(state="normal")
    nentry.grid(row=4,columnspan=2,pady=15,ipadx=50,ipady=5)
    
        
    
        
    def fun():
        name1=nentry.get()
        pass1=passentry.get()
        confpass1=cpassentry.get()


        path1="C:/Users/Nakul/Desktop/python/signup/"
       
        namefile=os.listdir(path1)
        print(namefile)
        ext=name1+".txt"
        
        if ext in namefile:
            print("ok")
            passcheck=open(path1+ext,"r")
            passcheck1= passcheck.read()
            if passcheck1==pass1:
                window()
                

                
            elif confpass1!=pass1:
                clear()
                messagebox.showerror("","please check password")
                
            else:
                clear()
                messagebox.showwarning("warning","Invalid user")
            
            
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

    def window():
            
           rootwindow=tk.Tk()
           rootwindow.state("zoom")
           name1=nentry.get()
           name=tk.Label(rootwindow,text="hello "+name1)
           name.pack()
           rootlogin.destroy()
           rootwindow.mainloop()     
            

        
    password=tk.Label(rootlogin,text="PASSWORD",font="Arial 12 ")
    password.config(bg="black",fg="white",anchor="center")
    password.grid(row=5,columnspan=2,pady=15)

    passentry=tk.Entry(rootlogin,font="Arial 12 ")
    #passentry.insert(0,"Login Password")
    passentry.config(show="*")
    passentry.grid(row=6,columnspan=2,pady=15,ipadx=50,ipady=5)

    cpassword=tk.Label(rootlogin,text="CONFIRM PASSWORD",font="Arial 12 ")
    cpassword.config(bg="black",fg="white",anchor="center")
    cpassword.grid(row=7,columnspan=2,pady=15)

    cpassentry=tk.Entry(rootlogin,font="Arial 12 ")
    #cpassentry.insert(0,"Enter confirm password")
    cpassentry.config(show="*")
    cpassentry.grid(row=8,columnspan=2,pady=15,ipadx=50,ipady=5)


    sub=tk.Button(rootlogin,text="SUBMIT",height=2,width=15,bg="orange" ,fg="black",command=lambda:[fun()])
    #sub.grid(row=9,columnspan=1)
    sub.grid(row=10,column=0)
    

    can=tk.Button(rootlogin,text="CANCEL",height=2,bg="orange" ,fg="black",width=15)
    
    can.grid(row=10,column=1)
    
    
    
def signup():
    rootSignup=tk.Tk()
    rootSignup.configure(bg="black")
    rootSignup.state("zoom")
    
    subhome=tk.Button(rootSignup,text="HOME",height=2,width=15,bg="orange" ,fg="black",command=lambda:[rootSignup.destroy(),home()])
    subhome.grid(row=0,padx=10,pady=20)
      
    sym=tk.Label(rootSignup,text="---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
    sym.config(justify="center",bg="black",fg="black")
    sym.grid(row=1 , padx=20,pady=10)
    
    def fun2():
        uname=nentry.get()
        passwd=passentry.get()
        
        path="C:/Users/Nakul/Desktop/python/signup/"
        file=open(path+uname+".txt","w")
        file.write(passwd)

    def clear1():
        nentry.delete(0,'end')
        passentry.delete(0,'end')
        
    sign=tk.Label(rootSignup,text="SIGNUP FORM",font="Arial 14 bold ")
    sign.config(bg="black",fg="white",justify="center")
    sign.grid(row=2 , padx=20,pady=10)

    name=tk.Label(rootSignup,text="USER NAME",font="Arial 12 ")
    name.config(bg="black",fg="white",anchor="center")
    name.grid(row=3,pady=20)

    nentry=tk.Entry(rootSignup,font="Arial 12")
    #nentry.insert(0,"Enter username")
    #nentry.configure(state="normal")
    nentry.grid(row=4,padx=20,pady=20,ipadx=50,ipady=5)

    password=tk.Label(rootSignup,text="PASSWORD",font="Arial 12 ")
    password.config(bg="black",fg="white",anchor="center")
    password.grid(row=5,pady=20)

    passentry=tk.Entry(rootSignup,font="Arial 12 ")
    #passentry.insert(0,"Enter password")
    passentry.config(show="*")
    passentry.grid(row=6,padx=20,pady=20,ipadx=50,ipady=5)

    
    sub=tk.Button(rootSignup,text="SUBMIT",height=2,width=15,bg="orange" ,fg="black",command=lambda:[fun2(),clear1()])
    sub.grid(row=9,padx=10,pady=20)

    can=tk.Button(rootSignup,text="CANCEL",bg="orange" ,fg="black",height=2,width=15)
    can.grid(row=10,padx=10)

home()


