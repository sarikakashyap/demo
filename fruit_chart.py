import tkinter as tk
from tkinter import PhotoImage
from PIL import Image, ImageTk
root = tk.Tk()
'''pineapple=tk.PhotoImage(file="C:/Users/Nakul/Desktop/python/pineapple.png")
l=tk.Label(root,image=pineapple).pack()

cherry=ImageTk.PhotoImage(Image.open("C:/Users/Nakul/Desktop/python/cherry.jpg").resize((200,200)))
panel2=tk.Label(root, image=cherry).pack(side="left")
'''
root.geometry("1250x700")
root.maxsize(1250,700)
root.minsize(1250,700)
root.configure(bg="#999111")

ft=tk.Label(root, text="Fruit chart",font="Elephant 30 bold ",bg="#999111")
ft.grid(row=0,column=3 , sticky=" ")


apple =ImageTk.PhotoImage(Image.open("C:/Users/Nakul/Desktop/python/apple.jpg").resize((200,200)))
panel =tk.Label(root, image =apple,bg="#999111")
panel.grid(row=1,padx=20)
at=tk.Label(root, text="Apple" ,font="Elephant 30 bold ",bg="#999111")
at.grid(row=1,column=2)

banana=ImageTk.PhotoImage(Image.open("C:/Users/Nakul/Desktop/python/banana.jpg").resize((200,200)))
panel1=tk.Label(root,image=banana)
panel1.grid(row=2)

bt=tk.Label(root, text="Banana",font="Elephant 30 bold ",bg="#999111")
bt.grid(row=2,column=2 ,padx=20)

cherry=ImageTk.PhotoImage(Image.open("C:/Users/Nakul/Desktop/python/cherry.jpg").resize((200,200)))
panel2=tk.Label(root, image=cherry)
panel2.grid(row=3,padx=20)
ct=tk.Label(root, text="Cherry",font="Elephant 30 bold ",bg="#999111")
ct.grid(row=3,column=2)




kiwi=ImageTk.PhotoImage(Image.open("C:/Users/Nakul/Desktop/python/kiwi.jpg").resize((200,200)))
panel4=tk.Label(root,image=kiwi, padx=20)
panel4.grid(row=1 , column=3)

kt=tk.Label(root, text="Kiwi",font="Elephant 30 bold ",bg="#999111")
kt.grid(row=1,column=4)


guava=ImageTk.PhotoImage(Image.open("C:/Users/Nakul/Desktop/python/guava.jpg").resize((200,200)))
panel5=tk.Label(root, image=guava)
panel5.grid(row=2 , column=3)

gt=tk.Label(root, text="Guava",font="Elephant 30 bold ",bg="#999111")
gt.grid(row=2,column=4)



mango =ImageTk.PhotoImage(Image.open("C:/Users/Nakul/Desktop/python/mango.jpg").resize((200,200)))
panel6 =tk.Label(root, image =mango)
panel6.grid(row=3 , column=3)

mt=tk.Label(root, text="Mango",font="Elephant 30 bold ",bg="#999111")
mt.grid(row=3,column=4)






papaya=ImageTk.PhotoImage(Image.open("C:/Users/Nakul/Desktop/python/papaya.jpg").resize((200,200)))
panel8=tk.Label(root, image=papaya)
panel8.grid(row=1, column=5)

pt=tk.Label(root, text="Papaya",font="Elephant 30 bold ",bg="#999111")
pt.grid(row=1,column=6)


dragon =ImageTk.PhotoImage(Image.open("C:/Users/Nakul/Desktop/python/dragon.jpg").resize((200,200)))
panel3 =tk.Label(root, image =dragon)
panel3.grid(row=2,column=5)
dt=tk.Label(root, text="Dragon",font="Elephant 30 bold ",bg="#999111")
dt.grid(row=2,column=6)


orange=ImageTk.PhotoImage(Image.open("C:/Users/Nakul/Desktop/python/orange.jpg").resize((200,200)))
panel7=tk.Label(root,image=orange)
panel7.grid(row=3 , column=5)

ot=tk.Label(root, text="Orange",font="Elephant 30 bold ",bg="#999111")
ot.grid(row=3,column=6)




root.mainloop()
