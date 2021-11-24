import tkinter as tk
from tkinter import PhotoImage,IntVar

root = tk.Tk()
root.title("Simple GUI Application")
root.configure(bg="#ffffff")
root.state("zoomed")


l1= tk.Label(root, text="Simple Gui application", font = "Cambria 30 bold")
l1.configure(bg="orange", fg="white")
l1.grid(row=1)

img = tk.PhotoImage(file="C:/Users/Nakul/Desktop/python/wrong.png")
l2=tk.Label(root, image=img)
l2.grid(row=2,column=3)

but=tk.Button(root,text="Button",command=quit)
but.configure(bg="green",fg="red")
but.grid(row=2,column=2)

rad=tk.Radiobutton(root,text="First radio button",value=1,command=quit)
rad.configure(bg="white")
rad.grid(row=3,column=2)

def submit():
    a=var.get()
    l1= tk.Label(root,text=a,  font = "Cambria 30 bold")
    l1.configure(bg="orange", fg="white")
    l1.grid(row=5)
    

var=IntVar()
ch=tk.Checkbutton(root,text="First check button",variable=var,command=submit)
ch.configure(bg="red",fg="black")
ch.grid(row=4,column=2)
