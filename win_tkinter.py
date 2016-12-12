import tkinter as tk
from tkinter import messagebox
import database
import widgets
import os
from PIL import Image, ImageTk


class WinControlPanel:
    def __init__(self, img_window, coords, paths):
        self.root = tk.Tk()
        self.root.geometry("500x570+30+30")
        
        self.db = database.Database('docs_osborne', 'testuser', 'test123', ('sellos', 'documentos'))
        self.db.load_seals()

        self.coords = coords
        self.paths = paths
        self.path_index = 0
        
        # POINT 1 DISPLAY
        self.pt1_label = tk.Label(self.root, text="Point 1:")
        self.pt1_label.place(x=20, y=10)
        
        self.pt1x_value = tk.IntVar()
        self.pt1x_info = tk.Entry(self.root, state=tk.DISABLED, textvariable=self.pt1x_value)
        self.pt1x_info.place(x=70, y=10, width=50)
        self.pt1x_value.set(str(coords[0]))
        
        self.pt1y_value = tk.IntVar()
        self.pt1y_info = tk.Entry(self.root, state=tk.DISABLED, textvariable=self.pt1y_value)
        self.pt1y_info.place(x=130, y=10, width=50)
        self.pt1y_value.set(str(coords[1]))

        # POINT 2 DISPLAY
        self.pt2_label = tk.Label(self.root, text="Point 2:")
        self.pt2_label.place(x=20, y=30)
        
        self.pt2x_value = tk.IntVar()
        self.pt2x_info = tk.Entry(self.root, state=tk.DISABLED, textvariable=self.pt2x_value)
        self.pt2x_info.place(x=70, y=30, width=50)
        self.pt2x_value.set(str(coords[2]))
        
        self.pt2y_value = tk.IntVar()
        self.pt2y_info = tk.Entry(self.root, state=tk.DISABLED, textvariable=self.pt2y_value)
        self.pt2y_info.place(x=130, y=30, width=50)
        self.pt2y_value.set(str(coords[3]))

        # NEW SEAL WINDOW
        def on_new_seal():
            self.new_seal_win = WinNewSeal(self.db, img_window)
        self.new_seal_butt = tk.Button(self.root, text='New', command=on_new_seal)
        self.new_seal_butt.place(x=200, y=20)

        # SEAL SELECTION ITEMS
        self.seal_type_list = widgets.SealsList(self.root, self.db)
        self.seal_type_list.x = 20
        self.seal_type_list.y = 70
        self.seal_type_list.place_items()

        # OK BUTTON
        def on_ok_button():
            self.db.insert_document(self.paths[self.path_index],
                                    self.seal_type_list.curr_seal_type.get(),
                                    (self.pt1x_value.get(), self.pt1y_value.get(),
                                     self.pt2x_value.get(), self.pt2y_value.get()))

            if self.path_index < len(self.paths):
                self.path_index += 1
                onlyimages = [f for f in os.listdir(self.paths[self.path_index])
                              if os.path.isfile(os.path.join(self.paths[self.path_index], f)) and f.endswith('.png')]

                # Llamar método de ventana de pygame que actualiza a la nueva imagen
                if __name__ != "__main__":
                    img_window.update_img(self.paths[self.path_index] + '/' + onlyimages[0])
            else:
                messagebox.showinfo("End of classification", "There are no more documents to classify")

        self.ok_button = tk.Button(self.root, text='OK', command=on_ok_button)
        self.ok_button.place(x=250, y=20)

        def on_closing():
            if messagebox.askokcancel("Quit", "Do you want to quit?"):
                self.root.destroy()

        self.root.protocol("WM_DELETE_WINDOW", on_closing)

    def update_labels(self, new_coords):
        self.pt1x_value.set(str(new_coords[0]))
        self.pt1y_value.set(str(new_coords[1]))
        self.pt2x_value.set(str(new_coords[2]))
        self.pt2y_value.set(str(new_coords[3]))


class WinNewSeal:
    def __init__(self, db, img_win):
        self.db = db
        self.img_win = img_win

        self.root = tk.Tk()
        self.width = 300
        self.height = 100
        geom_str = "%ix%i+30+30" % (self.width, self.height)
        self.root.geometry(geom_str)

        # SEAL INFO
        self.name_label = tk.Label(self.root, text='Nombre')
        self.name_label.place(x=20, y=10)
        # self.seal_name = tk.StringVar()
        self.name_info = tk.Entry(self.root)  # , textvariable=self.seal_name)
        self.name_info.place(x=70, y=10)

        self.author_label = tk.Label(self.root, text='Autor')
        self.author_label.place(x=20, y=40)
        # self.seal_author = tk.StringVar()
        self.author_info = tk.Entry(self.root)  # , textvariable=self.seal_author)
        self.author_info.place(x=70, y=40)

        # SEAL PREVIEW
        # self.canvas = tk.Canvas(self.root, width=600, height=400)  # <--CANVAS
        # self.img_route = self.db.seal_list[0].img_route
        # self.img_route = self.img_route.replace("\\", "/")
        # photo = Image.open(self.img_route)
        # cropped = photo.crop((coords[0], coords[1], coords[2], coords[3]))
        # tk_cropped = ImageTk.PhotoImage(cropped)
        # # photo = tk.PhotoImage(file=self.img_route)
        # self.seal_img = self.canvas.create_image(0, 0, anchor=tk.NW, image=tk_cropped)
        # self.canvas.image = tk_cropped

        # OK BUTTON
        self.ok_button = tk.Button(self.root, text='OK', command=self.on_ok_button)
        self.ok_button.place(x=200, y=20)

    def on_ok_button(self):
        self.db.insert_seal(self.name_info.get(), self.author_info.get())
        self.img_win.save_seal(self.name_info.get())
        self.root.destroy()


if __name__ == "__main__":
    path = 'C:/Users/usuario/Desktop/Document'
    walk = os.walk(path)

    doc_paths = []
    for root, dirs, files in walk:
        there_is_any_img = False
        for curr_file in files:
            if curr_file.endswith(".png"):
                there_is_any_img = True

        if there_is_any_img:
            root = root.replace("\\", "/")
            doc_paths.append(root)

    win = WinControlPanel(None, (10, 20, 30, 40), doc_paths)
    while 1:
        win.root.update_idletasks()
        win.root.update()

