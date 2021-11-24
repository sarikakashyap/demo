import tkinter as tk
root = tk.Tk()
root.configure(bg="blue")

sym=tk.Label(root,text="---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
sym.config(justify="center",fg="blue",bg="blue")
sym.grid(row=1 , column=50, padx=20,pady=20)


sign=tk.Label(root,text="SIGNUP FORM",font="Arial 40 bold ")
sign.config(bg="blue",justify="center")
sign.grid(row=2 , column=50, padx=20,pady=20)

name=tk.Label(root,text="USER NAME",font="Arial 30 ")
name.config(bg="blue",anchor="center")
name.grid(row=3, column=50,pady=20)

nentry=tk.Entry(root,font="Arial 15 ")
nentry.insert(0,"Enter username")
nentry.configure(state="normal")
nentry.grid(row=4, column=50,padx=20,pady=20,ipadx=50,ipady=5)

password=tk.Label(root,text="PASSWORD",font="Arial 30 ")
password.config(bg="blue",anchor="center")
password.grid(row=5, column=50,pady=20)

passentry=tk.Entry(root,font="Arial 15 ")
passentry.grid(row=6, column=50,padx=20,pady=20,ipadx=50,ipady=5)

cpassword=tk.Label(root,text="CONFIRM PASSWORD",font="Arial 30 ")
cpassword.config(bg="blue",anchor="center")
cpassword.grid(row=7, column=50,pady=20)

passentry=tk.Entry(root,font="Arial 15 ")
passentry.grid(row=8, column=50,padx=20,pady=20,ipadx=50,ipady=5)

sub=tk.Button(root,text="SUBMIT",height=2,width=15)
sub.grid(row=9,column=50,padx=10,pady=20)

can=tk.Button(root,text="CANCEL",height=2,width=15)
can.grid(row=10,column=50,padx=10)


root.mainloop()
