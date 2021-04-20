from tkinter import *
from tkinter import messagebox
import random as r



def button(frame):       
    b=Button(frame,padx=6,pady=10,bg="Indigo",width=10,height=2,text="   ",font=('arial',15,'bold'),relief="sunken",bd=7)
    return b


def change():             
    global a
    for i in ['X','O']:
        if not(i==a):
            a=i
            break

def reset():                
    global a
    for i in range(5):
        for j in range(5):
                b[i][j]["text"]=" "
                b[i][j]["state"]=NORMAL
                p1.delete(0,"end")
                p2.delete(0,"end")
    a=r.choice(['X','O'])



#logic

def w_l():             
    for i in range(5):
        if(b[i][0]["text"]==b[i][1]["text"]==b[i][2]["text"]==b[i][3]["text"]==b[i][4]["text"]==a or 
        b[0][i]["text"]==b[1][i]["text"]==b[2][i]["text"]==b[3][i]["text"]==b[4][i]["text"]==a ):
            if a=='X':
                messagebox.showinfo("Congrats!!"," "+p1.get()+" '"+a+"' has won")
            if a=='O':
                messagebox.showinfo("Congrats!!"," "+p2.get()+" '"+a+"'has won")
            reset()
    if(b[0][0]["text"]==b[1][1]["text"]==b[2][2]["text"]==b[3][3]["text"]==b[4][4]["text"]==a or 
    b[0][4]["text"]==b[1][3]["text"]==b[2][2]["text"]==b[3][1]["text"]==b[4][0]["text"]==a):
        if a=='X':
                messagebox.showinfo("Congrats!!"," "+p1.get()+" '"+a+"' has won")
        if a=='O':
            messagebox.showinfo("Congrats!!"," "+p2.get()+" '"+a+"' has won")
        reset()
    elif(b[0][0]["state"]==b[0][1]["state"]==b[0][2]["state"]==b[0][3]["state"]==b[0][4]["state"]==b[1][0]["state"]==b[1][1]["state"]==b[1][2]["state"]==b[1][3]["state"]==b[1][4]["state"]==
    b[2][0]["state"]==b[2][1]["state"]==b[2][2]["state"]==b[2][3]["state"]==b[2][4]["state"]==b[3][0]["state"]==b[3][1]["state"]==b[3][2]["state"]==b[3][3]["state"]==b[3][4]["state"]==b[4][0]["state"]==b[4][1]["state"]==b[4][2]["state"]==b[4][3]["state"]==
    b[4][4]["state"]==DISABLED):
        messagebox.showinfo("Tied!!","The match ended in a draw")
        reset()

def click(row,col):
        b[row][col].config(text=a,state=DISABLED,disabledforeground=colour[a])
        w_l()
        change()
        if a=='X':
            person.config(text=p1.get()+"'s Chance")
        if a=='O':
            person.config(text=p2.get()+"'s Chance")


root=Tk()                   
root.title("Tic-Tac-Toe")   

a=r.choice(['X','O'])    
person=Label(text=a+"'s Chance",font=('arial',20,'bold'), justify=CENTER)
person.grid(row=9,column=0,columnspan=3)   
p1=StringVar()
p2=StringVar()


player1 = Label(text = 'Player 1 (X)', font=('Arial', 15, 'bold')) 
player1.grid(row=5,column=0) 
p1 = Entry(font=('Arial',10,'normal'))
p1.grid(row=5,column=1) 

player2 = Label(text = 'Player 2 (O)', font=('Arial', 15, 'bold')) 
player2.grid(row=7,column=0) 
p2 = Entry(font=('Arial',10,'normal'))
p2.grid(row=7,column=1) 

colour={'O':"yellow",'X':"White"}
b=[[],[],[],[],[]]
for i in range(5):
        for j in range(5):
                b[i].append(button(root))
                b[i][j].config(command= lambda row=i,col=j:click(row,col))
                b[i][j].grid(row=i,column=j)

root.mainloop()