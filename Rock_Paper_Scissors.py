from tkinter import *
import random
from tkinter import ttk
import tkinter.font as font

screen=Tk()
screen.title("Rock paper scissors")
screen.geometry("700x300")

lab1=Label(screen,text="Rock Paper Scissors",font=font.Font(size=20),fg="black")
lab2=Label(screen,text="Let's start the game...",fg="green")

lab1.pack()
lab2.pack()

screen.mainloop()