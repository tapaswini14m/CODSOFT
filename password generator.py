# ==========================================
#      ADVANCED PASSWORD GENERATOR
#          CODSOFT TASK - PYTHON
# ==========================================

import random
import string
import tkinter as tk
from tkinter import messagebox

# ---------------- PASSWORD FUNCTION ---------------- #

def generate_password():

    password = ""

    try:
        length = int(length_entry.get())

        if length <= 0:
            messagebox.showerror("Error", "Enter valid length!")
            return

        # Character sets
        lowercase = string.ascii_lowercase
        uppercase = string.ascii_uppercase
        digits = string.digits
        symbols = string.punctuation

        characters = ""

        if lower_var.get():
            characters += lowercase

        if upper_var.get():
            characters += uppercase

        if digit_var.get():
            characters += digits

        if symbol_var.get():
            characters += symbols

        if characters == "":
            messagebox.showwarning("Warning", "Select at least one option!")
            return

        # Generate password
        password = ''.join(random.choice(characters) for _ in range(length))

        password_entry.delete(0, tk.END)
        password_entry.insert(0, password)

    except ValueError:
        messagebox.showerror("Error", "Please enter numbers only!")

# ---------------- COPY FUNCTION ---------------- #

def copy_password():
    password = password_entry.get()

    if password:
        root.clipboard_clear()
        root.clipboard_append(password)
        root.update()
        messagebox.showinfo("Copied", "Password copied to clipboard!")

# ---------------- MAIN WINDOW ---------------- #

root = tk.Tk()
root.title("Advanced Password Generator")
root.geometry("500x500")
root.config(bg="#1e1e1e")

# ---------------- TITLE ---------------- #

title = tk.Label(
    root,
    text="ADVANCED PASSWORD GENERATOR",
    font=("Arial", 18, "bold"),
    bg="#1e1e1e",
    fg="cyan"
)

title.pack(pady=20)

# ---------------- LENGTH ---------------- #

length_label = tk.Label(
    root,
    text="Enter Password Length",
    font=("Arial", 12),
    bg="#1e1e1e",
    fg="white"
)

length_label.pack()

length_entry = tk.Entry(
    root,
    font=("Arial", 14),
    justify="center"
)

length_entry.pack(pady=10)

# ---------------- CHECKBOXES ---------------- #

lower_var = tk.IntVar(value=1)
upper_var = tk.IntVar(value=1)
digit_var = tk.IntVar(value=1)
symbol_var = tk.IntVar(value=1)

tk.Checkbutton(
    root,
    text="Include Lowercase",
    variable=lower_var,
    font=("Arial", 11),
    bg="#1e1e1e",
    fg="white",
    selectcolor="black"
).pack(anchor="w", padx=120)

tk.Checkbutton(
    root,
    text="Include Uppercase",
    variable=upper_var,
    font=("Arial", 11),
    bg="#1e1e1e",
    fg="white",
    selectcolor="black"
).pack(anchor="w", padx=120)

tk.Checkbutton(
    root,
    text="Include Numbers",
    variable=digit_var,
    font=("Arial", 11),
    bg="#1e1e1e",
    fg="white",
    selectcolor="black"
).pack(anchor="w", padx=120)

tk.Checkbutton(
    root,
    text="Include Symbols",
    variable=symbol_var,
    font=("Arial", 11),
    bg="#1e1e1e",
    fg="white",
    selectcolor="black"
).pack(anchor="w", padx=120)

# ---------------- BUTTON ---------------- #

generate_btn = tk.Button(
    root,
    text="Generate Password",
    font=("Arial", 13, "bold"),
    bg="cyan",
    fg="black",
    padx=10,
    pady=5,
    command=generate_password
)

generate_btn.pack(pady=25)

# ---------------- PASSWORD DISPLAY ---------------- #

password_entry = tk.Entry(
    root,
    font=("Arial", 16),
    justify="center",
    width=30,
    bd=5
)

password_entry.pack(pady=10)

# ---------------- COPY BUTTON ---------------- #

copy_btn = tk.Button(
    root,
    text="Copy Password",
    font=("Arial", 12, "bold"),
    bg="lime",
    fg="black",
    padx=10,
    pady=5,
    command=copy_password
)

copy_btn.pack(pady=15)

# ---------------- FOOTER ---------------- #

footer = tk.Label(
    root,
    text="CODSOFT Python Internship Task",
    font=("Arial", 10),
    bg="#1e1e1e",
    fg="gray"
)

footer.pack(side="bottom", pady=10)

# ---------------- RUN ---------------- #

root.mainloop()