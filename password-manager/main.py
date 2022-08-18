import json
from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import pyperclip


# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate_rand_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)

    if len(password_input.get()) == 0:
        password_input.insert(0, password)

    else:
        password_input.delete(0, END)
        password_input.insert(0, password)

    pyperclip.copy(password)
    # TODO: Find a solution to show info that password is copied to clipboard in async manner.


# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():
    website = website_input.get()
    email = email_username_input.get()
    password = password_input.get()
    new_data = {
        website: {
            "email": email,
            "password": password
        }
    }

    if len(website) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.showinfo(title='Oops', message="Please make sure you haven't left any fields empty.")
    else:
        try:
            with open("data.json", "r") as data_file:
                data = json.load(data_file)
        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        except json.decoder.JSONDecodeError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            data.update(new_data)
            with open("data.json", "w") as data_file:
                json.dump(data, data_file, indent=4)
        finally:
            website_input.delete(0, END)
            email_username_input.delete(0, END)
            password_input.delete(0, END)

# --------------------------------------- FETCH RECORD --------------------------- #


def fetch_record():
    website_name = website_input.get()
    if len(website_name) == 0:
        messagebox.showinfo(title='Oops', message=f'Please provide website name.')
    else:
        try:
            with open("data.json", "r") as data_file:
                json_data = json.load(data_file)
                record = json_data[website_name]
                messagebox.showinfo(title=website_name, message=f"Email/Username: {record['email']}\n"
                                                                f"Password: {record['password']}")
                # Added copy to clip board feature when user search for password in system.
                pyperclip.copy(record['password'])
                messagebox.showinfo(title=website_name, message=f"Password for email {record['email']} "
                                                                f"copied to clipboard")
        except FileNotFoundError:
            with open("data.json", "w"):
                messagebox.showerror(title='Error', message='No Data File Found.')
                pass
        except KeyError:
            messagebox.showerror(title='Error', message=f'Invalid website {website_name}.\nPlease try again..')


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
website_input.grid(column=1, row=1)

search_button = Button(text="Search", command=fetch_record, width=10)
search_button.grid(column=2, row=1)

email_username_label = Label(text="Email/Username:")
email_username_label.grid(column=0, row=2)

email_username_input = Entry(width=35)
email_username_input.grid(column=1, row=2)

password_label = Label(text="Password:")
password_label.grid(column=0, row=3)

password_input = Entry(width=35)
password_input.grid(column=1, row=3)

generate_button = Button(text="Generate Password", command=generate_rand_password, width=15)
generate_button.grid(column=2, row=3)

add_button = Button(width=15, text="Add", command=save)
add_button.grid(column=1, row=4)

window.mainloop()
