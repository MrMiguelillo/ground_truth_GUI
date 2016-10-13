import tkinter

top = tkinter.Tk()

startframe = tkinter.Frame(top)
C = tkinter.Canvas(startframe, height=400, width=600)

startframe.pack()
C.pack()

photo = tkinter.PhotoImage(name=r'D:\PycharmProjects\Ground_truth_GUI\python-logo.gif')
top.photo = photo
C.create_image((50, 50), image=photo, anchor='nw')

# label = tkinter.Label(image=photo)
# label.image = photo # keep a reference!
# label.pack()

# coord = 10, 50, 240, 210
# arc = C.create_arc(coord, start=0, extent=180, fill="red")

top.mainloop()
