import tkinter as tk
screen=tk.Tk()
screen.title("Weight Converter")
screen.geometry("800x800")
screen.configure(bg="orange")


def convert_weight():
    kg=int(e1.get())
    grams=kg*1000
    pounds=kg*2.2
    ounces=kg*35.2
    e2.delete(0,tk.END)
    e2.insert(tk.END,grams)
    e3.delete(0,tk.END)
    e3.insert(tk.END,pounds)
    e4.delete(0,tk.END)
    e4.insert(tk.END,ounces)
  
    

l1=tk.Label(text= "Weight Converter", width= 25, height=2, bg="grey",fg="black", font=("Arial",20))
l1.place(x=200,y=10)
l2=tk.Label(text= "Enter your weight in kg", width= 20, height=1, bg="grey",fg="black", font=("Arial",12))
l2.place(x=100,y=150)
e1=tk.Entry(width=20)
e1.place(x=400,y=150)
b1=tk.Button(text= "Convert", width= 15, height=1, bg="black",fg="white", font=("Arial",20),command=convert_weight)
b1.place(x=270,y=250)
l3=tk.Label(text= "grams", width= 10, height=1, bg="black",fg="white", font=("Arial",20))
l3.place(x=75,y=350)
l4=tk.Label(text= "pounds", width= 10, height=1, bg="black",fg="white", font=("Arial",20))
l4.place(x=300,y=350)
l5=tk.Label(text= "ounces", width= 10, height=1, bg="black",fg="white", font=("Arial",20))
l5.place(x=550,y=350)
e2=tk.Entry(width=20)
e2.place(x=75,y=450)
e3=tk.Entry(width=20)
e3.place(x=300,y=450)
e4=tk.Entry(width=20)
e4.place(x=550,y=450)
screen.mainloop()