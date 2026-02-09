from tkinter import *
import random
import os
from tkinter import messagebox
def generate():
    letters = list('abcdefghijklmnopqrstuvwxyz')
    chars = ['{','}','[',']','(',')','*','&','^','%','$','#','@','!']
    numbers = list('0123456789')
    a = 7
    b = 2
    c = 7
    password_chars = []
    for _ in range(a):
        password_chars.append(random.choice(letters))
    for _ in range(b):
        password_chars.append(random.choice(chars))
    for _ in range(c):
        password_chars.append(random.choice(numbers))
    random.shuffle(password_chars)
    final_password = "".join(password_chars)
    pass_input.delete(0, END)
    pass_input.insert(0, final_password)

def save():
    website_val = web_input.get().strip()
    username_val = mail_input.get().strip()
    password_val = pass_input.get().strip()
    if len(website_val) == 0 or len(username_val) == 0:
        messagebox.showwarning(title="Oops",message="Sorry, but you haven't filled one of the things")
    else :
        is_ok = messagebox.askokcancel(title="Confirmation",message=f"For Confirmation you have entered\n your website name = {website_val}\n Email/username = {username_val}\n password = {password_val}\n is this ok ?")
        if is_ok:
         file_path = r"E:\Udemy Full course\Password_Manager\password.txt"
         os.makedirs(os.path.dirname(file_path), exist_ok=True)
         with open(file_path, mode="a") as file:
              file.write(f"Website = {website_val} , Email/Username = {username_val} , password = {password_val}\n")
def find():
    website_val = web_input.get().strip()
    if len(website_val) == 0:
        messagebox.showwarning(title="Oops", message="Website is empty")
        return

    file_path = r"E:\Udemy Full course\Password_Manager\password.txt"

    with open(file_path, mode="r") as file:
        for line in file:
            if line.lower().startswith(f"website = {website_val.lower()}"):
                password = line.split("password =")[1].strip()
                messagebox.showinfo(title=website_val, message=f"Password: {password}")
                return

    messagebox.showinfo(title="Not Found", message="No password found for that website.")


window = Tk()
window.config(padx=200, pady=200)

canva = Canvas(width=400, height=424)
canva.pack()

img_path = r"E:\Udemy Full course\Password_Manager\79a4d5aa-c5ca-44c2-b4c0-16b736a978ff.png"
if os.path.exists(img_path):
    pass_image = PhotoImage(file=img_path)
    canva.create_image(206, 212, image=pass_image)

website_lbl = Label(text="Website", font=("Arial", 11, "bold"))
website_lbl.place(x=-80, y=370)
web_input = Entry(width=30)
web_input.place(x=160, y=380)
find= Button(text="Find", command=find)
find.place(x=400, y=380)


mail_lbl = Label(text="Email Address / Username", font=("Arial", 11, "bold"))
mail_lbl.place(x=-80, y=420)
mail_input = Entry(width=30)
mail_input.place(x=160, y=420)

password_lbl = Label(text="Password", font=("Arial", 11, "bold"))
password_lbl.place(x=-80, y=460)
pass_input = Entry(width=30)
pass_input.place(x=160, y=460)

gen = Button(text="Generate", command=generate)
gen.place(x=400, y=460)

saved = Button(text="Save", command=save)
saved.place(x=200, y=530)

window.mainloop()
