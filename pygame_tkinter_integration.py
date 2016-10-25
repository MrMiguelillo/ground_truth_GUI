import os
import win_pygame


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

doc_win = win_pygame.WinPygame(doc_paths)

while 1:
    doc_win.main_loop()
    doc_win.control_panel.root.update()
    doc_win.control_panel.root.update_idletasks()

