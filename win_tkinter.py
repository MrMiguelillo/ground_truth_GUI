import tkinter as tk
import database
import widgets


root = tk.Tk()
root.geometry("400x500+30+30")

db = database.Database('docs_osborne', 'testuser', 'test123', ('sellos', 'documentos'))
db.load_seals()

# POINT 1 DISPLAY
pt1_label = tk.Label(root, text="Point 1:")
pt1_label.place(x=20, y=10)

pt1x_value = tk.StringVar()
pt1x_info = tk.Entry(root, state=tk.DISABLED, textvariable=pt1x_value)
pt1x_info.place(x=70, y=10, width=50)
pt1x_value.set("hola")

pt1y_value = tk.StringVar()
pt1y_info = tk.Entry(root, state=tk.DISABLED, textvariable=pt1y_value)
pt1y_info.place(x=130, y=10, width=50)
pt1y_value.set("hola")


# POINT 2 DISPLAY
pt2_label = tk.Label(root, text="Point 2:")
pt2_label.place(x=20, y=30)

pt2x_value = tk.StringVar()
pt2x_info = tk.Entry(root, state=tk.DISABLED, textvariable=pt2x_value)
pt2x_info.place(x=70, y=30, width=50)
pt2x_value.set("hola")

pt2y_value = tk.StringVar()
pt2y_info = tk.Entry(root, state=tk.DISABLED, textvariable=pt2y_value)
pt2y_info.place(x=130, y=30, width=50)
pt2y_value.set("hola")


# SEAL TYPE LIST
seal_type_list = widgets.SealsList(root, db)
seal_type_list.init_option_menu()
seal_type_list.x = 20
seal_type_list.y = 70
seal_type_list.place_items()

# type_label = tk.Label(root, text="Type:")
# type_label.place(x=20, y=70)
#
# OPTIONS = [seal.name for seal in db.seal_list]
#
# curr_seal_type = tk.StringVar(root)
# curr_seal_type.set(OPTIONS[0])  # initial value
#
#
# def onChangeItem():
#     index = OPTIONS.index(curr_seal_type.get())
#     # change image
#     path = db.seal_list[0].img_route
#     path = path.replace("\\", "/")
#     img = tk.PhotoImage(file=path)
#     seal_canvas.itemconfig(seal_img, image=img)
#
# option = tk.OptionMenu(root, curr_seal_type, *OPTIONS, command=onChangeItem())
#
#
# option.place(x=55, y=70)
# SEAL PROTOTYPE DISPLAY
# img_route = db.seal_list[0].img_route
# img_route = img_route.replace("\\", "/")
# photo = tk.PhotoImage(file=img_route)
# seal_label = tk.Label(image=photo)
# seal_label.image = photo
# seal_label.place(x=55, y=150)
#
#
# def button_callback(label, options_var):
#     index = [(i,seal) for (i, seal) in enumerate(db.seal_list) if seal.name == options_var.get()]
#     photo_path = db.seal_list[index[0][0]].img_route  # this is dirty code. names have to change for readability
#     photo_path = photo_path.replace("\\", "/")
#     p = tk.PhotoImage(file=photo_path)
#     label.image = p
#
#
# button = tk.Button(root, text='OK', command=button_callback(seal_label, curr_seal_type))
# seal_canvas = tk.Canvas(root, width=300, height=300)
# seal_canvas.place(x=55, y=150)
# img_route = db.seal_list[0].img_route
# img_route = img_route.replace("\\", "/")
# photo = tk.PhotoImage(file=img_route)
# seal_img = seal_canvas.create_image(0, 0, anchor=tk.NW, image=photo)

root.mainloop()

# TODO: make seal image label change acording to which seal is currently selected
# TODO: add 'new seal' button plus its corresponding form
