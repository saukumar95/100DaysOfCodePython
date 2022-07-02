from tkinter import *

window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=350, height=150)
window.config(padx=20, pady=20)

blank_label = Label(text="")
blank_label.grid(column=0, row=0)
blank_label.config(padx=50)

user_input = Entry(width=10)
user_input.insert(END, string="0")
user_input.grid(column=1, row=0)

miles_label = Label(text="Miles")
miles_label.grid(column=2, row=0)

is_equal_to_label = Label(text="is equal to")
is_equal_to_label.grid(column=0, row=1)

result = 0
result_label = Label(text="0")
result_label.grid(column=1, row=1)

km_label = Label(text="Km")
km_label.grid(column=2, row=1)


def calculate_miles_to_km():
    miles = float(user_input.get())
    result_label.config(text=f"{miles*1.61}")


def reset():
    result_label.config(text="0")


calculate_button = Button(text="Calculate", command=calculate_miles_to_km)
calculate_button.grid(column=1, row=2)

clear_button = Button(text="Clear", command=reset)
clear_button.grid(column=2, row=2)

window.mainloop()