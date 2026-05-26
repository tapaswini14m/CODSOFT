# ================================
#      GUI CALCULATOR PROJECT
# ================================

# =========================================
#       SCIENTIFIC CALCULATOR IN PYTHON
# =========================================

from tkinter import *
import math

# Create Window
root = Tk()
root.title("Scientific Calculator")
root.geometry("500x650")
root.config(bg="black")

# Entry Box
entry = Entry(root,
              width=25,
              font=("Arial", 24),
              bd=10,
              relief=RIDGE,
              justify=RIGHT)

entry.grid(row=0, column=0, columnspan=5, pady=20)

# Functions
def click(value):
    current = entry.get()
    entry.delete(0, END)
    entry.insert(END, current + str(value))

def clear():
    entry.delete(0, END)

def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, END)
        entry.insert(END, result)
    except:
        entry.delete(0, END)
        entry.insert(END, "Error")

def square_root():
    try:
        result = math.sqrt(float(entry.get()))
        entry.delete(0, END)
        entry.insert(END, result)
    except:
        entry.delete(0, END)
        entry.insert(END, "Error")

def square():
    try:
        result = float(entry.get()) ** 2
        entry.delete(0, END)
        entry.insert(END, result)
    except:
        entry.delete(0, END)
        entry.insert(END, "Error")

def sin():
    try:
        result = math.sin(math.radians(float(entry.get())))
        entry.delete(0, END)
        entry.insert(END, result)
    except:
        entry.delete(0, END)
        entry.insert(END, "Error")

def cos():
    try:
        result = math.cos(math.radians(float(entry.get())))
        entry.delete(0, END)
        entry.insert(END, result)
    except:
        entry.delete(0, END)
        entry.insert(END, "Error")

def tan():
    try:
        result = math.tan(math.radians(float(entry.get())))
        entry.delete(0, END)
        entry.insert(END, result)
    except:
        entry.delete(0, END)
        entry.insert(END, "Error")

def log():
    try:
        result = math.log10(float(entry.get()))
        entry.delete(0, END)
        entry.insert(END, result)
    except:
        entry.delete(0, END)
        entry.insert(END, "Error")

# Buttons
buttons = [
    ('7',1,0), ('8',1,1), ('9',1,2), ('/',1,3), ('C',1,4),
    ('4',2,0), ('5',2,1), ('6',2,2), ('*',2,3), ('√',2,4),
    ('1',3,0), ('2',3,1), ('3',3,2), ('-',3,3), ('x²',3,4),
    ('0',4,0), ('.',4,1), ('=',4,2), ('+',4,3), ('log',4,4),
    ('sin',5,0), ('cos',5,1), ('tan',5,2)
]

# Create Buttons
for (text, row, col) in buttons:

    if text == "=":
        Button(root, text=text, width=8, height=3,
               font=("Arial",14), bg="green", fg="white",
               command=calculate).grid(row=row, column=col)

    elif text == "C":
        Button(root, text=text, width=8, height=3,
               font=("Arial",14), bg="red", fg="white",
               command=clear).grid(row=row, column=col)

    elif text == "√":
        Button(root, text=text, width=8, height=3,
               font=("Arial",14),
               command=square_root).grid(row=row, column=col)

    elif text == "x²":
        Button(root, text=text, width=8, height=3,
               font=("Arial",14),
               command=square).grid(row=row, column=col)

    elif text == "sin":
        Button(root, text=text, width=8, height=3,
               font=("Arial",14),
               command=sin).grid(row=row, column=col)

    elif text == "cos":
        Button(root, text=text, width=8, height=3,
               font=("Arial",14),
               command=cos).grid(row=row, column=col)

    elif text == "tan":
        Button(root, text=text, width=8, height=3,
               font=("Arial",14),
               command=tan).grid(row=row, column=col)

    elif text == "log":
        Button(root, text=text, width=8, height=3,
               font=("Arial",14),
               command=log).grid(row=row, column=col)

    else:
        Button(root, text=text, width=8, height=3,
               font=("Arial",14),
               command=lambda t=text: click(t)).grid(row=row, column=col)

# Run App
root.mainloop()