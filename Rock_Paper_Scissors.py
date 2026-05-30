from tkinter import *
import random
from tkinter import ttk
import tkinter.font as font

screen=Tk()
screen.title("Rock paper scissors")
screen.geometry("700x300")

ys=0
ls=0
def compchoice():
    comp_input=random.choice(["Rock","Paper","Scissors"])
    return comp_input

def tie():
    global ys, ls
    lab2.config(text="Tie!")
    us.config(text="Your score:"+str(ys))
    cs.config(text="Computer score:"+str(ls))

def pw():
    global ys, ls
    lab2.config(text="You win!")
    us+=1
    us.config(text="Your score:"+str(ys))
    cs.config(text="Computer score:"+str(ls))
    
def cw():
    global ys, ls
    lab2.config(text="Computer wins!")
    cs+=1
    us.config(text="Your score:"+str(ys))
    cs.config(text="Computer score:"+str(ls))

def playerchoice(player_input):
    comp_input=compchoice()
    u.config(text="You selected:"+player_input)
    comp.config(text="Computer selected:"+comp_input)
     
    if comp_input==player_input:       
        tie()
    elif comp_input=="rock" and player_input=="paper" or comp_input=="scissors" and player_input=="rock" or comp_input=="paper" and player_input=="scissors":
        pw()
    else:
        cw()

lab1=Label(screen,text="Rock Paper Scissors",font=font.Font(size=20),fg="black")
lab1.pack()

lab2=Label(screen,text="Let's start the game...",fg="green",font=font.Font(size=15))
lab2.pack()

frame1=Frame(screen)
frame1.pack()

lab3=Label(frame1,text="Your Options:",fg="black",pady=8,font=font.Font(size=12))
lab3.grid(row=0,column=0,pady=8)
    
rock=Button(frame1,text="Rock",pady=5,font=font.Font(size=20),fg="black",width=5,bd=0,bg="pink", command=playerchoice("Rock"))
rock.grid(row=1,column=1,padx=8,pady=5)

paper=Button(frame1,text="Paper",pady=5,font=font.Font(size=20),fg="black",width=5,bd=0,bg="purple",command=playerchoice("Paper"))
paper.grid(row=1,column=2,padx=8,pady=5)

scissors=Button(frame1,text="Scissors",pady=5,font=font.Font(size=20),fg="black",width=6,bd=0,bg="blue",command=playerchoice("Scissors"))
scissors.grid(row=1,column=3,padx=8,pady=5)

score=Label(frame1,text="Score:",font=font.Font(size=12))
score.grid(row=2,column=0,padx=8,pady=5)

u=Label(frame1,text="You selected:")
u.grid(row=2,column=1,padx=8,pady=5)

comp=Label(frame1,text="Computer selected:")
comp.grid(row=3,column=1,padx=8,pady=5)

us=Label(frame1,text="Your score:")
us.grid(row=2,column=2,padx=8,pady=5)

cs=Label(frame1,text="Computer score:")
cs.grid(row=3,column=2,padx=8,pady=5)


screen.mainloop()
