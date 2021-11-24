import tkinter as tk
import os
from tkinter import Frame, messagebox
global loginbutt
global signbut


global name1,confpass1,pass1


def home():
    root = tk.Tk()
    root.configure(bg="black")
    root.state("zoom")
    root.iconbitmap("C:/Users/Nakul/Desktop/python/agt_login.ico")
    root.title("HOME")
    login_frame=Frame(root,bg='black')
    Signup_frame=Frame(root,bg='black')
    login_frame.pack()
    Signup_frame.pack()
       
        
    loginbutt=tk.Button(login_frame,text="LOGIN ",height=3,width=10,font="Arial 12 bold",bg="orange" ,fg="black",command=lambda :[root.destroy(),login()])
    loginbutt.pack(pady=200)
    loginbutt.config(justify="center" , padx=50)

    signbut=tk.Button(Signup_frame,text="SIGNUP",height=3,width=10,font="Arial 12 bold",bg="orange" ,fg="black",command=lambda :[root.destroy(),signup()])
    signbut.pack()
    signbut.config(justify="center" , padx=50)
    root.mainloop()

        
def login():
    rootlogin=tk.Tk()
    rootlogin.configure(bg="black")
    rootlogin.state("zoom")
    rootlogin.title("Login") 
    rootlogin.iconbitmap("C:/Users/Nakul/Desktop/python/login.ico")
    home_frame=Frame(rootlogin,bg="black")
    home_frame.pack()

    login_page_frame=Frame(rootlogin,bg='black')
    login_page_frame.pack()

    login_button_frame=Frame(rootlogin,bg="black")
    login_button_frame.pack()
   
    
    subhome2=tk.Button(home_frame,text="HOME",height=2,width=15,bg="orange" ,fg="black",command=lambda:[rootlogin.destroy(),home()])  
    subhome2.pack( pady=50)

    login=tk.Label(login_page_frame,text="LOGIN FORM",font="Arial 14 bold ")
    login.config(bg="black",fg="white",justify="center")
    login.pack(ipady=50)

    name=tk.Label(login_page_frame,text="USER NAME",font="Arial 12 ")
    name.config(bg="black",fg="white",anchor="center")
    name.pack()

    nentry=tk.Entry(login_page_frame,font="Arial 12 ")
    nentry.pack()
    
    
        
    
        
    def fun():
        #fetching entry from the entry field
        name1=nentry.get() 
        pass1=passentry.get()
        confpass1=cpassentry.get()


        path1="C:/Users/Nakul/Desktop/python/signup/"  #path where all the file store
       
        namefile=os.listdir(path1) # have all the file name
        #print(namefile)
        ext=name1+".txt"  
        
        if ext in namefile: # if the username file exist  run this block
            #print("ok")
            passcheck=open(path1+ext,"r") #open the file in read mode
            passcheck1= passcheck.read()
            
            if (passcheck1==pass1) and (confpass1==pass1): # if password and confirm password matches move to the next window
                
                path="C:/Users/Nakul/Desktop/python/signup/"
                #this login.txt file maintain record who is login successfully 
                file=open(path+"/login.txt","a") #open file in append mode

                #writting records           
                uname=file.write("UserName:"+name1+"\t\t")
                #print(uname)
                file.write("Password:"+pass1+"\t\t")
                file.write("Confirm Password:"+confpass1+"\n")
                file.write("----------------------------------------------------------------------------------------------------------------\n")              
                window()
                

                
            elif (confpass1!=pass1) or (passcheck1!=pass1): # if confirm password not matches with password or password is not correct
                
                messagebox.showerror("","please check password") #display message box
                       
            
        else:
            #print("no")
            clear()
            messagebox.showwarning("warning","User is not Register")

    #this clear function deleting the entry 
    def clear():
        nentry.delete(0,'end')
        passentry.delete(0,'end')
        cpassentry.delete(0,'end')
    
    # when user is successfully login this function execute
    def window():
            
           rootwindow=tk.Tk()
           rootwindow.state("zoom")
           name1=nentry.get()
           name=tk.Label(rootwindow,text="hello "+name1) # this window display message hello with user name
           name.pack()
           rootlogin.destroy()
           rootwindow.mainloop()     
            

        
    password=tk.Label(login_page_frame,text="PASSWORD",font="Arial 12 ")
    password.config(bg="black",fg="white",anchor="center")
    password.pack()
    

    passentry=tk.Entry(login_page_frame,font="Arial 12 ")
    passentry.config(show="*")
    passentry.pack()
    
    cpassword=tk.Label(login_page_frame,text="CONFIRM PASSWORD",font="Arial 12 ")
    cpassword.config(bg="black",fg="white",anchor="center")
    cpassword.pack()
    

    cpassentry=tk.Entry(login_page_frame,font="Arial 12 ")
    cpassentry.config(show="*")
    cpassentry.pack()

    sub=tk.Button(login_button_frame,text="SUBMIT",height=2,width=15,bg="orange" ,fg="black",command=lambda:[fun()])
    sub.config(padx=40)
    sub.pack(pady=50)
    
    

    can=tk.Button(login_button_frame,text="CANCEL",height=2,bg="orange" ,fg="black",width=15)
    can.config(padx=40)
    can.pack()
    
    
    
    
def signup():
    #this page was designed without Frame
    rootSignup=tk.Tk()
    rootSignup.configure(bg="black")
    rootSignup.state("zoom")
    rootSignup.iconbitmap("C:/Users/Nakul/Desktop/python/login_photo.ico")
    rootSignup.title("Signup") 
     
    home_frame=Frame(rootSignup,bg="black")
    home_frame.pack()
    
    signup_page=Frame(rootSignup,bg='black')
    signup_page.pack()

    button_frame=Frame(rootSignup,bg='black')
    button_frame.pack()
    
    subhome=tk.Button(home_frame,text="HOME",height=2,width=15,bg="orange" ,fg="black",command=lambda:[rootSignup.destroy(),home()])
    subhome.pack(pady=50)
      
        
    def fun2():
        uname=nentry.get()
        passwd=passentry.get()
        
        path="C:/Users/Nakul/Desktop/python/signup/"
        file=open(path+uname+".txt","w")
        file.write(passwd)

    def clear1():
        nentry.delete(0,'end')
        passentry.delete(0,'end')
        
    sign=tk.Label(signup_page,text="SIGNUP FORM",font="Arial 14 bold ")
    sign.config(bg="black",fg="white",justify="center")
    sign.pack(ipady=50)

    name=tk.Label(signup_page,text="USER NAME",font="Arial 12 ")
    name.config(bg="black",fg="white",anchor="center")
    name.pack(ipady=10)

    nentry=tk.Entry(signup_page,font="Arial 12")
    nentry.pack()

    password=tk.Label(signup_page,text="PASSWORD",font="Arial 12 ")
    password.config(bg="black",fg="white",anchor="center")
    password.pack(ipady=10)

    passentry=tk.Entry(signup_page,font="Arial 12 ")
    passentry.config(show="*")
    passentry.pack()

    
    sub=tk.Button(button_frame,text="SUBMIT",height=2,width=15,bg="orange" ,fg="black",command=lambda:[fun2(),clear1()])
    sub.config(padx=40)
    sub.pack(pady=50)

    can=tk.Button(button_frame,text="CANCEL",bg="orange" ,fg="black",height=2,width=15)
    can.pack()
    can.config(padx=40)
home()


