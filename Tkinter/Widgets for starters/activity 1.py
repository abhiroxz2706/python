from tkinter import *
from datetime import date
window=Tk()
window.title("My first app")
window.geometry("500x500")
lbl=Label(text="Hey there")
lbl.pack()
lbl2=Label(text="Enter your name")
lbl2.pack()
e=Entry()
e.pack()
def disp():
    name=e.get()
    message="Welcome buddy \n"
    greet="Good morning " + name + "\n"
    t.insert(END, message)
    t.insert(END, greet)
    t.insert(END, date.today())

btn=Button(text="click",command=disp)
btn.pack()
t=Text(height=5)
t.pack()
window.mainloop()