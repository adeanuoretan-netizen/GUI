import tkinter as tk
import random
from tkinter import messagebox
screen=tk.Tk()
screen.title("Guess the number game")
screen.geometry("800x800")
screen.configure(bg="brown")
computer_number=random.randint(1,20)
attempts=4
def guess_the_number():
    guess=int(e1.get())
    global computer_number,attempts
    if guess>computer_number:
        messagebox.showinfo("Hint","GO LOWER!")
    elif computer_number>guess:
        messagebox.showinfo("Hint","GO HIGHER")
    else:
        messagebox.showinfo("You win","CONGRATULATIONS")
    attempts-=1
    l3.config(text="Attempts:"+str(attempts))
    if attempts==0:
        screen.destroy()







#messagebox.showinfo("Details","I'm thinking of a number between 1 and 20 can you guess it")

l1=tk.Label(text= "Guess the number game", width= 25, height=2, bg="grey",fg="black", font=("Arial",20))
l1.place(x=150,y=100)
l4=tk.Label(text= "I'm thinking of a number between 1 and 20 can you guess it", width= 50, height=2, bg="grey",fg="black", font=("Arial",12))
l4.place(x=50,y=200)
l2=tk.Label(text= "Take a guess", width= 25, height=2, bg="grey",fg="black", font=("Arial",20))
l2.place(x=50,y=300)
e1=tk.Entry(width=20)
e1.place(x=500,y=300)
b1=tk.Button(text= "Guess", width= 15, height=2, bg="black",fg="white", font=("Arial",20),command=guess_the_number)
b1.place(x=100,y=450)
l3=tk.Label(text= "Attemps:4", width= 25, height=2, bg="grey",fg="black", font=("Arial",20))
l3.place(x=50,y=550)





screen.mainloop()