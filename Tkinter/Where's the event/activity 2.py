from tkinter import *
from tkinter import messagebox

root=Tk()
root.geometry("200x200")

def msg():
    # messagebox.showwarning("Alert","Stop! Virus Found.")
    # messagebox.showinfo("Alert","Stop! Virus Found.")
    # messagebox.showerror("Alert","Stop! Virus Found.")
    # messagebox.askquestion("Alert","Stop! Virus Found.")
    # messagebox.askokcancel("Alert","Stop! Virus Found.")
    # messagebox.askyesno("Alert","Stop! Virus Found.")
    messagebox.askretrycancel("Alert","Stop! Virus Found.")

button=Button(root,text="Scan for virus", command=msg)
button.place(x=40,y=80)

root.mainloop()