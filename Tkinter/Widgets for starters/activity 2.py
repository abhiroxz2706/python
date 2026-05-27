from tkinter import *
from datetime import date
window=Tk()
window.title("Product of 2 numbers")
window.geometry("500x500")
n1=Label(text="Enter the number 1")
n1.pack()
e_1=Entry()
e_1.pack()
n2=Label(text="Enter the number 2")
n2.pack()
e_2=Entry()
e_2.pack()
def disp():
    x=e_1.get()
    y=e_2.get()
    z=int(x)*int(y)
    t.insert(END, z)
    
btn=Button(text="click",command=disp)
btn.pack()
t=Text(height=5)
t.pack()
window.mainloop()