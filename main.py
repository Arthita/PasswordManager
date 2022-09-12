from cgitb import text
from random import randint
import tkinter
from tkinter import messagebox
import json
import os 
BGCOLOR = '#FFEEAD'

DIR=os.path.dirname(__file__)


def generate_password():
    import random
    letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
    digits = '0123456789'
    signs = '!#$%&*()-+'
    temp = []
    a = random.randint(2, 4)
    b = random.randint(2, 4)
    c = random.randint(2, 4)
    for i in range(a):
        temp.append(random.choice(letters))
    for i in range(b):
        temp.append(random.choice(digits))
    for i in range(c):
        temp.append(random.choice(signs))
    random.shuffle(temp)
    new_password = ''.join(temp)
    password1.insert(0, new_password)


def save_details():
    if website1.get() == '' or email1.get() == '' or password1.get() == '':
        messagebox.showerror(title='Error', message='Some fields are empty')
        return
    new_dict = {
        website1.get(): {
            'email': email1.get(),
            'password': password1.get()
        }
    }
    flag = messagebox.askokcancel(title=website1.get(
    ), message=f'Details entered:\n{email1.get()}\n{password1.get()}\nIs it ok to save?')
    if flag:
        try:
            with open((f'{DIR}\details.json'), 'r') as file:
                data = json.load(file)
                data.update(new_dict)
        except:
            with open((f'{DIR}\details.json'), 'w') as file:
                json.dump(new_dict, file, indent=4)
        else:
            with open((f'{DIR}\details.json'), 'w') as file:
                json.dump(data, file, indent=4)
        website1.delete(0, tkinter.END)
        password1.delete(0, tkinter.END)


def search():
    try:
        with open((f'{DIR}\details.json')) as file:
            data = json.load(file)
    except:
        messagebox.showinfo(
            title='Warning', message='Data file does not exist')
    else:
        if website1.get() in data:
            e = data[website1.get()]['email']
            p = data[website1.get()]['password']
            email1.insert(0, e)
            password1.insert(0, p)
        else:
            messagebox.showinfo(
                title='Warning', message='There is no such website saved before')


window = tkinter.Tk()
window.config(padx=30, pady=30, bg=BGCOLOR)
window.title('Password Manager')
canvas = tkinter.Canvas(height=200, width=200,
                        highlightthickness=0, bg=BGCOLOR)
img = tkinter.PhotoImage(
    file=(f'{DIR}\logo.png'))
canvas.create_image(100, 100, image=img)
canvas.grid(column=1, row=0)
website = tkinter.Label(text='Website', bg=BGCOLOR)
website.grid(column=0, row=1)
website1 = tkinter.Entry(width=30)
website1.focus()
website1.grid(column=1, row=1, columnspan=2)
search = tkinter.Button(text='Search', fg='white',
                        bg='brown', width=14, command=search)
search.grid(column=3, row=1)
email = tkinter.Label(text='Email', bg=BGCOLOR)
email.grid(column=0, row=2)
email1 = tkinter.Entry(width=30)
email1.insert(0, 'abcd@gmail.com')
email1.grid(column=1, row=2, columnspan=2)
password = tkinter.Label(text='Password', bg=BGCOLOR)
password.grid(column=0, row=3)
password1 = tkinter.Entry(width=30)
password1.grid(column=1, row=3, columnspan=2)
generate = tkinter.Button(text='Generate Password',
                          fg='white', bg='brown', command=generate_password)
generate.grid(column=3, row=3)
add = tkinter.Button(text='Add', fg='white', bg='red',
                     width=20, command=save_details)
add.grid(column=1, row=4, columnspan=2)
tkinter.mainloop()
