from tkinter import *

window = Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)

my_label = Label(text="I Am a Label", font=("Arial", 24, "bold"))
my_label.pack()

my_label.config(text="New Text")
my_label.grid(column=0, row=0)


def button_clicked():
    my_label.config(text=f"{user_input.get()}")


button = Button(text="Click Me", command=button_clicked)
button.grid(column=1, row=1)


user_input = Entry(width=10)
user_input.grid(column=2, row=2)

button_new = Button(text="Click me again", command=button_clicked)
button_new.grid(column=2, row=0)


window.mainloop()