import tkinter as tk


class SealsList:
    def __init__(self, master, db):
        self.db = db
        self.x = 0
        self.y = 0
        self.label = tk.Label(master, text='Type:')

        self.OPTIONS = [seal.name for seal in self.db.seal_list]
        self.curr_seal_type = tk.StringVar(master)
        self.curr_seal_type.set(self.OPTIONS[0])
        self.option_menu = tk.OptionMenu(master, self.curr_seal_type, *self.OPTIONS, command=None)

        self.canvas = tk.Canvas(master, width=300, height=300)
        self.img_route = db.seal_list[0].img_route
        self.img_route = self.img_route.replace("\\", "/")
        photo = tk.PhotoImage(file=self.img_route)
        self.seal_img = self.canvas.create_image(0, 0, anchor=tk.NW, image=photo)

    def on_change_item(self):
        index = self.OPTIONS.index(self.curr_seal_type.get())
        # change image
        path = self.db.seal_list[0].img_route
        path = path.replace("\\", "/")
        photo = tk.PhotoImage(file=path)
        self.canvas.itemconfig(self.seal_img, image=photo)

    def init_option_menu(self):
        self.option_menu.configure(command=self.on_change_item())
