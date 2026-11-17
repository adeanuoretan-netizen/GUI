import tkinter as tk
import datetime
screen=tk.Tk()
screen.title("Digital Calender")
screen.geometry("600x600")
screen.configure(bg="light blue")

def show_calender():
    current_time=datetime.datetime.now()
    x=current_time.strftime("%d/%m/%Y")
    print(current_time)
    l1.config(text=x )


 
b1=tk.Button(text= "Show Date", width= 25, height=2, bg="black",fg="white", font=("Arial",20),command=show_calender)
b1.place(x=120,y=150)
l1=tk.Label(text= "", width= 25, height=2, bg="grey",fg="black", font=("Arial",20))
l1.place(x=120,y=250)



screen.mainloop()