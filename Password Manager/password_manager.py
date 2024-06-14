import tkinter as tk
from tkinter import messagebox  # Serve para aparecer popups no gui!!
from os import path
import random
import pyperclip  # Serve para quando selecionar uma string já fica copiada, e posso usar logo CTRL+V
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
# pyinstaller --onefile --windowed --add-data="logo.png;." password_manager.py
LETTERS: tuple = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                  'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
                  'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z')
NUMBERS: tuple = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9')
SYMBOLS: tuple = ('!', '#', '$', '%', '&', '(', ')', '*', '+', ' ')

nr_letters = random.randint(8, 10)
nr_symbols = random.randint(2, 4)
nr_numbers = random.randint(2, 4)


def button_generate():
    password_entry.delete(0, tk.END)
    password: list = list(f'{''.join(random.sample(LETTERS, nr_letters))}'
                          f'{''.join(random.sample(NUMBERS, nr_numbers))}'
                          f'{''.join(random.sample(SYMBOLS, nr_symbols))}')
    random.shuffle(password)
    password_entry.insert(0, ''.join(password))
    pyperclip.copy(''.join(password))


# ---------------------------- SAVE PASSWORD ------------------------------- #
if not path.exists('all_password.txt'):
    with open('all_password.txt', 'w', encoding='utf-8') as output_file:
        pass


def button_add():
    new_data = {
        website_entry.get().title(): {
            'email': email_entry.get(),
            'password': password_entry.get(),
        }
    }
    if 0 in (len(password_entry.get()), len(website_entry.get())):
        messagebox.showinfo('Oops', "Please don't leave any fields empty")
    elif tk.messagebox.askokcancel(f'{website_entry.get().title()}', f'These are the details entered:\nEmail:'
                                                                     f'{email_entry.get()}\nPassword:{password_entry.get()}'
                                                                     f'\nIt is ok to save?'):
        # with open('all_password.txt', 'a', encoding='utf-8') as file:
        #     file.write(' | '.join([website_entry.get().title(), email_entry.get(), f'{password_entry.get()}\n']))

        try:
            with open('all_password.json', 'r', encoding='utf-8') as file:
                data = json.load(file)
        except (FileNotFoundError, json.decoder.JSONDecodeError):
            with open('all_password.json', 'w', encoding='utf-8') as file:
                json.dump(new_data, file, indent=4)
        else:
            data.update(new_data)

            with open('all_password.json', 'w', encoding='utf-8') as file:
                json.dump(data, file, indent=4)

        finally:
            # Clear entry fields after successful save (optional)
            website_entry.delete(0, tk.END)
            password_entry.delete(0, tk.END)


# ------------------------- Search Button ----------------------------- #


def button_search():
    with open('all_password.json') as file:
        try:
            data_websites: dict = json.load(file)
            # for row in file:
            #     data_websites[row.split(' | ')[0]] = row.split(' | ')[1:]
        except json.decoder.JSONDecodeError:
            messagebox.showinfo(title='Error', message='Ainda não existe uma password nesse Website')

        else:
            if website_entry.get().title().strip() in data_websites.keys():
                variable = website_entry.get().title().strip()
                messagebox.showinfo(title=variable, message=f'Email: {data_websites[variable]['email']}\n'
                                                            f'Password: {data_websites[variable]['password']}')
            else:
                messagebox.showinfo(title=website_entry.get().title(), message='Ainda não existe uma password nesse '
                                                                               'Website')


# ---------------------------- UI SETUP ------------------------------- #
window = tk.Tk()
window.title('Password Manager')
window.config(padx=30, pady=40)
window.minsize(width=570, height=420)
window.maxsize(width=570, height=420)

canvas = tk.Canvas(width=200, height=200)
logo_image = tk.PhotoImage(file=path.join(path.dirname(__file__), "logo.png"))
canvas.create_image(100, 189//2, image=logo_image)
canvas.grid(row=0, column=0, columnspan=3)

tk.Label(text='Website:', font=('Arial', 17, 'bold')).grid(row=1, column=0, sticky='w')
tk.Label(text='Email/Username:', font=('Arial', 17, 'bold')).grid(row=2, column=0, sticky='w')
tk.Label(text='Password:', font=('Arial', 17, 'bold')).grid(row=3, column=0, sticky='w')

website_entry = tk.Entry(width=37, highlightthickness=1)
website_entry.grid(row=1, column=1, sticky='ew')

search_button = tk.Button(text='Search', font=('Arial', 12), command=button_search, highlightthickness=1)
search_button.grid(row=1, column=2, sticky='ew')

email_entry = tk.Entry(width=50, highlightthickness=1)
email_entry.insert(0, 'cmmonteiro40@gmail.com')
email_entry.grid(row=2, column=1, columnspan=2)

password_entry = tk.Entry(width=32, highlightthickness=1)
password_entry.grid(row=3, column=1, sticky='ew')

generate_button = tk.Button(text='Genarate', font=('Arial', 12), command=button_generate, highlightthickness=1)
generate_button.grid(row=3, column=2, sticky='e')

add_button = tk.Button(text='Add', font=('Arial', 12), command=button_add, highlightthickness=1)
add_button.grid(row=4, column=1, columnspan=2, sticky='ew')

window.mainloop()
