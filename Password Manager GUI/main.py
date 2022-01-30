from tkinter import *
from tkinter import messagebox
import random
import pyperclip
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    #Password Generator Project

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_letters = [random.choice(letters) for _ in range(nr_letters)]
    password_symbols = [random.choice(symbols) for _ in range(nr_symbols)]
    password_numbers = [random.choice(numbers) for _ in range(nr_numbers)]

    password_list = password_letters + password_symbols + password_numbers

    random.shuffle(password_list)
    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)
# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    if len(website) == 0 or len(password) == 0:
        messagebox.showerror(title="Error", message="Don't leave entries blank")
    else:
        is_ok = messagebox.askokcancel(title=website,
                                   message=f"These are the details entered : \n Email : {email}\n Pasword : {password}\n Is it ok to save ?")
        if is_ok:
            with open("data.txt", "a") as data_file:
                data_file.write(f"{website}  || {email}  || {password} \n")
                website_entry.delete(0, END)
                password_entry.delete(0, END)
                website_entry.focus()

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Passsword Manager")
window.config(padx=40, pady=50)

canvas = Canvas(height=200, width=200)
logo_img = PhotoImage(file='logo.png')

canvas.create_image(100, 100, image= logo_img)
canvas.grid(column=1, row=0)

#Labels
website_label = Label(text="Website : ")
website_label.grid(row=1, column=0)
email_label = Label(text="Username/email : ")
email_label.grid(row=2, column=0)
password_label = Label(text="Password : ")
password_label.grid(row=3, column=0)

#Entries
website_entry = Entry(width=42)
website_entry.grid(column=1, row=1, columnspan=2)
website_entry.focus()
email_entry = Entry(width=42)
email_entry.grid(column=1, row=2, columnspan=2)
email_entry.insert(0, "name@email.com")
password_entry = Entry(width=21)
password_entry.grid(column=1, row=3)

#Buttons
generate_password_button = Button(text="Generate Password", command=generate_password)
generate_password_button.grid(column=2, row=3)
add_button = Button(text="Add", width=36, pady=5, command=save)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()
