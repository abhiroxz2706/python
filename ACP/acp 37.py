from tkinter import *

window = Tk()
window.title("Getting started with widgets")
window.geometry("400x300")

intro = Label(text="This application takes two numbers and returns their product.")
intro.pack()

n_1 = Label(text="Enter the first number")
n_1.pack()

n_1_entry = Entry()
n_1_entry.pack()

n_2 = Label(text="Enter the second number")
n_2.pack()

n_2_entry = Entry()
n_2_entry.pack()

result_label = Label(text="")
result_label.pack()

def get_product():
    num1 = int(n_1_entry.get())
    num2 = int(n_2_entry.get())
    product = num1 * num2
    print(product)

button = Button(text="Multiply", command=get_product)
button.pack()

window.mainloop()