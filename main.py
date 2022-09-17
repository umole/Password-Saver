from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import pyperclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    pass_letters = [choice(letters) for _ in range(randint(8, 10))]
    pass_numbers = [choice(numbers) for _ in range(randint(2, 4))]
    pass_symbols = [choice(symbols) for _ in range(randint(2, 4))]

    password_list = pass_letters + pass_numbers + pass_symbols

    shuffle(password_list)

    password = "".join(password_list)

    pass_entry.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_pass():
    website_name = website_entry.get()
    email_name = email_entry.get()
    pass_name = pass_entry.get()

    new_data = {
        website_name: {
            "email": email_name,
            "Password": pass_name,
        }
    }

    if len(website_name) == 0 or len(email_name) == 0 or len(pass_name) == 0:
        messagebox.showinfo(title="Error", message="field cannot be left empty")

    else:
        is_correct = messagebox.askyesno(website_name, message=f"website: {website_name} \nemail: "
                                                  f"{email_name} \npassword: {pass_name} \nIs this correct?")
        if is_correct:
            try:
                with open("data.json", "r") as file:
                    data = json.load(file)
            except FileNotFoundError:
                with open("data.json", "w") as file:
                    json.dump(new_data, file, indent=4)
            else:
                data.update(new_data)
                with open("data.json", "w") as file:
                    json.dump(data, file, indent=4)
            finally:
                website_entry.delete(0, END)
                pass_entry.delete(0, END)
                website_entry.focus()


def search_account():
    website = website_entry.get()
    try:
        with open("data.json", "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="Not found")
    else:
        if website in data:
            email = data[website]['email']
            password = data[website]["Password"]
            messagebox.showinfo(title=website, message=f"Email= {email}\n Password = {password}")
        else:
            messagebox.showinfo(title="Error", message="Account doesn't exist")

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200, highlightthickness=0)
logo_png = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_png)
canvas.grid(column=1, row=0)

#Labels
website_Label = Label(text="Website:")
website_Label.grid(column=0, row=1)
email_label = Label(text="Email/Username:")
email_label.grid(column=0, row=2)
pass_label = Label(text="Password:")
pass_label.grid(column=0, row=3)

#Entries
website_entry = Entry(width=31)
website_entry.grid(column=1, row=1, columnspan=1)
website_entry.focus()
email_entry = Entry(width=50)
email_entry.grid(column=1, row=2, columnspan=2)
email_entry.insert(0, "ozimedeumole@gmail.com")
pass_entry = Entry(width=31)
pass_entry.grid(column=1, row=3)

#buttons
search_button = Button(text="Search", width=14, command=search_account)
search_button.grid(column=2, row=1)

gen_pass_button = Button(text="Generate Password", command=generate_password)
gen_pass_button.grid(column=2, row=3)

add_acc_button = Button(text="Add", width=43, command=save_pass)
add_acc_button.grid(column=1, row=4, columnspan=2)



window.mainloop()