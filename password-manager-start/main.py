from tkinter import *
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #


def get_user_inputs():
    with open("data.txt", "a") as data:
        data.write(f"\n{website_input.get()} | {email_username_input.get()} | {password_input.get()}\n")


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)


canvas = Canvas(width=200, height=200)
pm_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=pm_img)
canvas.grid(column=1, row=0)

website_label = Label(text="Website:")
website_label.grid(column=0, row=1)

website_input = Entry(width=35)
website_input.focus()
website_input.grid(column=1, row=1, columnspan=2)

email_username_label = Label(text="Email/Username:")
email_username_label.grid(column=0, row=2)

email_username_input = Entry(width=35)
email_username_input.grid(column=1, row=2, columnspan=2)

password_label = Label(text="Password:")
password_label.grid(column=0, row=3)

password_input = Entry(width=21)
password_input.grid(column=1, row=3)

generate_button = Button(text="Generate Password")
generate_button.grid(column=2, row=3)

add_button = Button(width=36, text="Add", command=get_user_inputs)
add_button.grid(column=1, row=4, columnspan=2)


window.mainloop()