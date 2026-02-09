from tkinter import *

window = Tk()
window.title("First Tkinter")
window.minsize(width=200, height=300)

def button_clicked():
    my_label.config(text="Button got Clicked")

my_label = Label(text="New File")
my_label.pack()

button = Button(text="Click me", command=button_clicked)
button.pack()

window.mainloop()
