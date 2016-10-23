import win_tkinter
import win_pygame


doc_win = win_pygame.WinPygame()
# control_panel = win_tkinter.WinControlPanel()

while 1:
    doc_win.main_loop()
    doc_win.control_panel.root.update()
    doc_win.control_panel.root.update_idletasks()

