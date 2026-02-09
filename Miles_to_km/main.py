from tkinter import *

window = Tk()
window.minsize(width=200, height=200)

my_label = Label(text="Miles to Kilometer Converter")
my_label.pack()

def convert():
    a = float(inp.get())
    output.config(text=f"{a * 1.6} KM")

inp = Entry(width=20)
inp.pack()

output = Label(text="")
output.pack()

button = Button(text="Convert", command=convert)
button.pack()

window.mainloop()
