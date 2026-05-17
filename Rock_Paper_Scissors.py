from tkinter import *
import random
from tkinter import ttk
import tkinter.font as font

screen=Tk()
screen.title("Rock paper scissors")
screen.geometry("700x300")

lab1=Label(screen,text="Rock Paper Scissors",font=font.Font(size=20),fg="black")
lab2=Label(screen,text="Let's start the game...",fg="green",font=font.Font(size=15))
frame1=Frame(screen)
lab3=Label(frame1,text="Your Options:",fg="black",pady=8,font=font.Font(size=12))    
rock=Button(frame1,text="Rock",pady=5,font=font.Font(size=20),fg="black",width=5,bd=0,bg="pink")
paper=Button(frame1,text="Paper",pady=5,font=font.Font(size=20),fg="black",width=5,bd=0,bg="purple")
scissors=Button(frame1,text="Scissors",pady=5,font=font.Font(size=20),fg="black",width=6,bd=0,bg="blue")
score=Label(frame1,text="Score:",font=font.Font(size=12))
u=Label(frame1,text="You selected:")
comp=Label(frame1,text="Computer selected:")
us=Label(frame1,text="Your score:")
cs=Label(frame1,text="Computer selected:")

lab1.pack()
lab2.pack()
frame1.pack()
lab3.grid(row=0,column=0,pady=8)
rock.grid(row=1,column=1,padx=8,pady=5)
paper.grid(row=1,column=2,padx=8,pady=5)
scissors.grid(row=1,column=3,padx=8,pady=5)
score.grid(row=2,column=0,padx=8,pady=5)
u.grid(row=2,column=1,padx=8,pady=5)
comp.grid(row=3,column=1,padx=8,pady=5)
us.grid(row=2,column=2,padx=8,pady=5)
cs.grid(row=3,column=2,padx=8,pady=5)

screen.mainloop()
