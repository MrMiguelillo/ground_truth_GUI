import win_tkinter
import win_pygame


doc_win = win_pygame.WinPygame()
control_panel = win_tkinter.WinTkinter()

while 1:
    doc_win.main_loop()
    control_panel.root.update()
    control_panel.root.update_idletasks()

