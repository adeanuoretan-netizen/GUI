import tkinter as tk
import datetime
screen=tk.Tk()
screen.title("Digital Clock")
screen.geometry("600x600")
screen.configure(bg="yellow")

def get_time():
    current_time=datetime.datetime.now()
    x=current_time.strftime("%H:%M:%S")
    print(current_time)
    l1.config(text=x )
    l1.after(1000,get_time)
    
b1=tk.Button(text= "Show Time", width= 25, height=2, bg="black",fg="white", font=("Arial",20),command=get_time)
b1.place(x=120,y=250)
l1=tk.Label(text= "", width= 25, height=2, bg="grey",fg="black", font=("Arial",20))
l1.place(x=120,y=350)


screen.mainloop()