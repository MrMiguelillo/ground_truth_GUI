import tkinter as tk
from tkinter import messagebox

top = tk.Tk()

def helloCallBack():
   tk.messagebox.showinfo("Hello Python", "Hello World")

B = tk.Button(top, text="Hello", command=helloCallBack)

B.pack()
top.mainloop()
