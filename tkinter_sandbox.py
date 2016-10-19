import tkinter as tk

# OptionMenu(master, variable, *values)

OPTIONS = [
    "egg",
    "bunny",
    "chicken"
]

master = tk.Tk()

var = tk.StringVar(master)
var.set(OPTIONS[0])  # initial value

option = tk.OptionMenu(master, var, *OPTIONS)
option.pack()
tk.mainloop()
