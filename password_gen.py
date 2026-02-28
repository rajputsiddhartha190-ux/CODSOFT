import tkinter as tk
from tkinter import messagebox
import secrets
import string

def generate_and_fill():
    chars = string.ascii_letters + string.digits + "@#$%"
    password = ''.join(secrets.choice(chars) for i in range(16))
    entry_new.delete(0, tk.END)
    entry_new.insert(0, password)
    entry_confirm.delete(0, tk.END)

def check_match():
    p1 = entry_new.get()
    p2 = entry_confirm.get()

    if p1 == p2 and p1 != "":
        messagebox.showinfo("Success", "Password matched!")
    else:
        messagebox.showinfo("Error","Password do not match!")

def toggle_password():
    if show_pass_var.get():
        entry_new.config(show="")
        entry_confirm.config(show="")
    else:
        entry_new.config(show="*")
        entry_confirm.config(show="*")

#UI SETUP
root = tk.Tk()
root.title("Creative Password Generator")
root.geometry("400x500")
root.configure(background= "#1e1e2e")
root.resizable(width=False, height=False)

#FONTS DESCRIBE
title_font=("Verdana",16, "bold")
label_font=("Arial",10)
btn_font = ("Arial",10,"bold")

#TITLE
tk.Label(root, text="🔐SECURE GENERATOR", font=title_font,
         bg="#1e1e2e",fg="#cba6f7").pack(pady=25)

#INPUT FIELDS
tk.Label(root, text="New Password", font=label_font, bg="#1e1e2e", fg="white").pack()
entry_new = tk.Entry(root, show="*", width=25, font=("Arial", 12), bd=3)
entry_new.pack(pady=10)

tk.Label(root, text="Confirm Password", font=label_font, bg="#1e1e2e", fg="white").pack()
entry_confirm = tk.Entry(root, show="*", width=25, font=("Arial", 12), bd=3)
entry_confirm.pack(pady=10)

#CHECKBOX
show_pass_var= tk.BooleanVar()
tk.Checkbutton(root, text="Show Passwords", variable=show_pass_var, command=toggle_password,
               bg="#1e1e2e", fg="white", selectcolor="#313244", activebackground="#1e1e2e").pack(pady=5)



btn_check = tk.Button(root, text="CHECK MATCH", command=check_match,
                      bg="#f38ba8", fg="black", font=btn_font, width=20, height=2, cursor="hand2")
btn_check.pack(pady=15)


btn_gen= tk.Button(root, text="GENERATE PASSWORD", command=generate_and_fill,
                   bg="#89dceb", fg="black", font=btn_font, width =20, height=2, cursor="hand2")
btn_gen.pack(pady=10)

root.mainloop()
