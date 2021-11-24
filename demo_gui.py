import tkinter as tk
root=tk.Tk()
root.geometry("900x500")
root.maxsize(1000,500)
l1=tk.Label(root , text="label one" , font=" Algerian 30 bold " )
l1.configure(bg="pink" ,fg="black")
l1.grid(row=1)
l2=tk.Label(root , text="Lable second", font="jokerman  60 bold underline italic ")
l2.configure(bg="yellow",fg="red")
l2.grid(row=4,column=2)

root.mainloop()
