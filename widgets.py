import tkinter as tk
from tkinter import messagebox


class SealsList:
    def __init__(self, master, db):
        self.db = db
        self.x = 0
        self.y = 0
        self.label = tk.Label(master, text='Type:')  # <--LABEL

        self.OPTIONS = [seal.name for seal in self.db.seal_list]
        self.curr_seal_type = tk.StringVar(master)
        self.curr_seal_type.set(self.OPTIONS[0])
        self.option_menu = tk.OptionMenu(master, self.curr_seal_type, *self.OPTIONS)  # <--OPTION MENU

        self.canvas = tk.Canvas(master, width=600, height=400)  # <--CANVAS
        self.img_route = self.db.seal_list[0].img_route
        self.img_route = self.img_route.replace("\\", "/")
        photo = tk.PhotoImage(file=self.img_route)
        self.seal_img = self.canvas.create_image(0, 0, anchor=tk.NW, image=photo)
        self.canvas.image = photo

        self.change_button = tk.Button(master, text="Change", command=self.on_change_item)

    def on_change_item(self):
        index = self.OPTIONS.index(self.curr_seal_type.get())
        # change image
        path = self.db.seal_list[index].img_route
        path = path.replace("\\", "/")
        photo = tk.PhotoImage(file=path)
        self.canvas.itemconfig(self.seal_img, image=photo)
        self.canvas.image = photo

    def place_items(self):
        self.label.place(x=self.x, y=self.y)
        self.option_menu.place(x=self.x + 35, y=self.y)
        self.canvas.place(x=self.x + 35, y=self.y + 80)
        self.change_button.place(x=self.x + 160, y=self.y+3)
