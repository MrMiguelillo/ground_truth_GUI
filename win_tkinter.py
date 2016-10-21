import tkinter as tk
import database
import widgets


class WinTkinter:
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("700x570+30+30")
        
        self.db = database.Database('docs_osborne', 'testuser', 'test123', ('sellos', 'documentos'))
        self.db.load_seals()
        
        # POINT 1 DISPLAY
        self.pt1_label = tk.Label(self.root, text="Point 1:")
        self.pt1_label.place(x=20, y=10)
        
        self.pt1x_value = tk.StringVar()
        self.pt1x_info = tk.Entry(self.root, state=tk.DISABLED, textvariable=self.pt1x_value)
        self.pt1x_info.place(x=70, y=10, width=50)
        self.pt1x_value.set("hola")
        
        self.pt1y_value = tk.StringVar()
        self.pt1y_info = tk.Entry(self.root, state=tk.DISABLED, textvariable=self.pt1y_value)
        self.pt1y_info.place(x=130, y=10, width=50)
        self.pt1y_value.set("hola")

        # POINT 2 DISPLAY
        self.pt2_label = tk.Label(self.root, text="Point 2:")
        self.pt2_label.place(x=20, y=30)
        
        self.pt2x_value = tk.StringVar()
        self.pt2x_info = tk.Entry(self.root, state=tk.DISABLED, textvariable=self.pt2x_value)
        self.pt2x_info.place(x=70, y=30, width=50)
        self.pt2x_value.set("hola")
        
        self.pt2y_value = tk.StringVar()
        self.pt2y_info = tk.Entry(self.root, state=tk.DISABLED, textvariable=self.pt2y_value)
        self.pt2y_info.place(x=130, y=30, width=50)
        self.pt2y_value.set("hola")

        # SEAL SELECTION ITEMS
        self.seal_type_list = widgets.SealsList(self.root, self.db)
        # self.seal_type_list.init_option_menu()
        self.seal_type_list.x = 20
        self.seal_type_list.y = 70
        self.seal_type_list.place_items()


if __name__ == "__main__":
    win = WinTkinter()
    while 1:
        win.root.update_idletasks()
        win.root.update()

# TODO: Transform this into a class
# TODO: add 'new seal' button plus its corresponding form
