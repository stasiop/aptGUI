from tkinter import *
import os
import subprocess
import tkinter as tk
window = Tk()
window.title("Welcome to aptGUI")
window.geometry('225x80')
password = tk.StringVar()
sudo = tk.StringVar()
txt = Entry(window,width=10,textvariable=password)
txt.grid(column=2, row=0)
def clicked():
    lbl = Label(window, text=password.get())
    lbl.grid(column=1, row=2)
    subprocess.call(["pkexec", "apt", "install", password.get(), "-y"])
def clicked1():
    subprocess.call(["pkexec", "apt","remove", password.get(), "-y"])
btn = Button(window, text="run apt install", command=clicked)
btn.grid(column=1, row=0)
btn = Button(window, text="run apt remove", command=clicked1)
btn.grid(column=1, row=1)
window.mainloop()

