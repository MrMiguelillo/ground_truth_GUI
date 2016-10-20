import tkinter as tk


class SealsList:
    def __init__(self, master, db):
        self.db = db
        self.x = 0
        self.y = 0
        self.label = tk.Label(master, text='Type:')  # <--LABEL

        self.OPTIONS = [seal.name for seal in self.db.seal_list]
        self.curr_seal_type = tk.StringVar(master)
        self.curr_seal_type.set(self.OPTIONS[0])
        self.option_menu = tk.OptionMenu(master, self.curr_seal_type, *self.OPTIONS, command=None) # <--OPTION MENU

        self.canvas = tk.Canvas(master, width=300, height=300)  # <--CANVAS
        self.img_route = self.db.seal_list[0].img_route
        self.img_route = self.img_route.replace("\\", "/")
        photo = tk.PhotoImage(file=self.img_route)
        self.seal_img = self.canvas.create_image(0, 0, anchor=tk.NW, image=photo)
        self.canvas.image = photo

    def on_change_item(self):
        index = self.OPTIONS.index(self.curr_seal_type.get())
        # change image
        path = self.db.seal_list[index].img_route
        path = path.replace("\\", "/")
        photo = tk.PhotoImage(file=path)
        self.canvas.itemconfig(self.seal_img, image=photo)
        self.canvas.image = photo

    def init_option_menu(self):
        self.option_menu.configure(command=self.on_change_item())

    def place_items(self):
        self.label.place(x=self.x, y=self.y)
        self.option_menu.place(x=self.x + 35, y=self.y)
        self.canvas.place(x=55, y=150)  # (x=self.x + 35, y=self.y + 80)
