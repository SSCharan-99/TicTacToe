from tkinter import *
from tkinter import messagebox
import random as r


def button(frame):       
    b=Button(frame,padx=2,bg="Indigo",width=3,text="   ",font=('arial',50,'bold'),relief="sunken",bd=5)
    return b


def change():             
    global a
    for i in ['X','O']:
        if not(i==a):
            a=i
            break

def reset():                
    global a
    for i in range(3):
        for j in range(3):
                b[i][j]["text"]=" "
                b[i][j]["state"]=NORMAL
    a=r.choice(['X','O'])



#logic

def w_l():             
    for i in range(3):
        if(b[i][0]["text"]==b[i][1]["text"]==b[i][2]["text"]==a or b[0][i]["text"]==b[1][i]["text"]==b[2][i]["text"]==a):
            if a=='X':
                messagebox.showinfo("Congrats!!","'"+p1.get()+"' has won")
            if a=='O':
                messagebox.showinfo("Congrats!!","'"+p2.get()+"' has won")
            reset()
    if(b[0][0]["text"]==b[1][1]["text"]==b[2][2]["text"]==a or b[0][2]["text"]==b[1][1]["text"]==b[2][0]["text"]==a):
        if a=='X':
                messagebox.showinfo("Congrats!!","'"+p1.get()+"' has won")
        if a=='O':
            messagebox.showinfo("Congrats!!","'"+p2.get()+"' has won")
        reset()
    elif(b[0][0]["state"]==b[0][1]["state"]==b[0][2]["state"]==b[1][0]["state"]==b[1][1]["state"]==b[1][2]["state"]==b[2][0]["state"]==b[2][1]["state"]==b[2][2]["state"]==DISABLED):
        messagebox.showinfo("Tied!!","The match ended in a draw")
        reset()

def click(row,col):
        b[row][col].config(text=a,state=DISABLED,disabledforeground=colour[a])
        w_l()
        change()
        person.config(text=a+"'s Chance")


root=Tk()                   
root.title("Tic-Tac-Toe")   

a=r.choice(['X','O'])    
person=Label(text=a+"'s Chance",font=('arial',20,'bold'))
person.grid(row=5,column=0,columnspan=3)   
p1=StringVar()
p2=StringVar()


player1 = Label(text = 'Player 1', font=('Arial', 15, 'bold')) 
player1.grid(row=3,column=0) 
p1 = Entry(font=('Arial',10,'normal'))
p1.grid(row=3,column=1) 

player2 = Label(text = 'Player 2', font=('Arial', 15, 'bold')) 
player2.grid(row=4,column=0) 
p2 = Entry(font=('Arial',10,'normal'))
p2.grid(row=4,column=1) 

colour={'O':"Yellow",'X':"White"}
b=[[],[],[]]
for i in range(3):
        for j in range(3):
                b[i].append(button(root))
                b[i][j].config(command= lambda row=i,col=j:click(row,col))
                b[i][j].grid(row=i,column=j)

root.mainloop()