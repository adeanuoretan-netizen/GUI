import tkinter as tk
screen=tk.Tk()
screen.title("Weight Converter")
screen.geometry("800x800")
screen.configure(bg="orange")


def convert_temperature():
    celcius=int(e1.get())
    fahrenheit=celcius*33.8
    e2.delete(0,tk.END)
    e2.insert(tk.END,fahrenheit)
  
    

l1=tk.Label(text= "Temperature Converter", width= 30, height=2, bg="grey",fg="black", font=("Arial",20))
l1.place(x=200,y=10)
l2=tk.Label(text= "Enter your Temperature in Celcius", width= 30, height=1, bg="grey",fg="black", font=("Arial",12))
l2.place(x=100,y=150)
e1=tk.Entry(width=20)
e1.place(x=400,y=150)
b1=tk.Button(text= "Convert", width= 15, height=1, bg="black",fg="white", font=("Arial",20),command=convert_temperature)
b1.place(x=270,y=250)
e2=tk.Entry(width=20)
e2.place(x=270,y=350)
screen.mainloop()