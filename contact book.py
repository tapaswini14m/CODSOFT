import tkinter as tk
from tkinter import messagebox

contacts = {}

# Add Contact
def add_contact():

    name = name_entry.get()
    phone = phone_entry.get()

    if name == "" or phone == "":
        messagebox.showwarning("Warning", "Enter all details")
        return

    contacts[name] = phone

    messagebox.showinfo("Success", "Contact Added")

    show_contacts()

# Show Contacts
def show_contacts():

    contact_list.delete(0, tk.END)

    for name, phone in contacts.items():
        contact_list.insert(tk.END, f"{name} : {phone}")

# Delete Contact
def delete_contact():

    selected = contact_list.get(tk.ACTIVE)

    if selected:
        name = selected.split(" : ")[0]

        del contacts[name]

        show_contacts()

# Main Window
root = tk.Tk()

root.title("Contact Book")
root.geometry("500x500")
root.config(bg="black")

# Title
title = tk.Label(
    root,
    text="CONTACT BOOK",
    font=("Arial", 20, "bold"),
    bg="black",
    fg="cyan"
)

title.pack(pady=20)

# Name
name_label = tk.Label(
    root,
    text="Enter Name",
    font=("Arial", 12),
    bg="black",
    fg="white"
)

name_label.pack()

name_entry = tk.Entry(
    root,
    font=("Arial", 14)
)

name_entry.pack(pady=10)

# Phone
phone_label = tk.Label(
    root,
    text="Enter Phone Number",
    font=("Arial", 12),
    bg="black",
    fg="white"
)

phone_label.pack()

phone_entry = tk.Entry(
    root,
    font=("Arial", 14)
)

phone_entry.pack(pady=10)

# Buttons
add_btn = tk.Button(
    root,
    text="Add Contact",
    font=("Arial", 12, "bold"),
    bg="cyan",
    fg="black",
    command=add_contact
)

add_btn.pack(pady=10)

delete_btn = tk.Button(
    root,
    text="Delete Contact",
    font=("Arial", 12, "bold"),
    bg="red",
    fg="white",
    command=delete_contact
)

delete_btn.pack(pady=10)

# Contact List
contact_list = tk.Listbox(
    root,
    font=("Arial", 13),
    width=40,
    height=10
)

contact_list.pack(pady=20)

# Run Window
root.mainloop()