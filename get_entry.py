import tkinter as tk  
from functools import partial  
from tkinter import messagebox as msg
   
'''   
def call_result(label_result, n1, n2):  
    num1 = (n1.get())  
    num2 = (n2.get())  
    result = int(num1)+int(num2)  
    label_result.config(text="Result = %d" % result)  
     
   
root = tk.Tk()  
root.geometry('400x200+100+200')  
  
root.title('Calculator')  
   
number1 = tk.StringVar()  
number2 = tk.StringVar()  
  
labelNum1 = tk.Label(root, text="A").grid(row=1, column=0)  
  
labelNum2 = tk.Label(root, text="B").grid(row=2, column=0)  
  
labelResult = tk.Label(root)  
  
labelResult.grid(row=7, column=2)  
  
entryNum1 = tk.Entry(root, textvariable=number1).grid(row=1, column=2)  
  
entryNum2 = tk.Entry(root, textvariable=number2).grid(row=2, column=2)  
  
call_result = partial(call_result, labelResult, number1, number2)  
  
buttonCal = tk.Button(root, text="Calculate", command=call_result).grid(row=3, column=0)  
  
root.mainloop()



'''

def entry():
    game_board=tk.Tk()
    play1_var=tk.StringVar()
    play2_var=tk.StringVar()
    play1=tk.Label(game_board,text="player1 Name")
    play1.place(x=10,y=110)
    play2=tk.Label(game_board,text="player2 Name")
    play2.place(x=10,y=150)
    play1_entry=tk.Entry(game_board,textvariable=play1_var)
    #play1_entry.insert(0,"player1 name ")
    play1_entry.place(x=95,y=110)
    play2_entry=tk.Entry(game_board,textvariable=play2_var)
    #play2_entry.insert(0,"player2 ")
    play2_entry.place(x=95,y=150)
    def create():
        p1=play1_var.get()
        p2=play2_var.get()
        play=tk.Label(game_board,text=p1)
        play.place(x=10,y=110)
        if not p1:
            msg.showerror(" "," please fill both the name")
        print(p1)
        print(p2)
        path="D:/data_bankManagement/game/"
        file1=open(path+"file1.txt","w")
        file1.write(p1+"\n"+p2)
    
    start=tk.Button(game_board,text=" Start ",command=create)
    start.place(x=105,y=30)

if __name__=='__main__':
    entry()
   
