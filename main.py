import os
import win_pygame

"""
main.py se encarga de proveer a las ventanas de una lista que contenga el directorio de cada una de las imágenes. Además
le pasa el índice para saber por qué imagen nos quedamos la última vez. También mantiene los bucles infinitos de las
ventanas
"""

path = 'C:/Users/usuario/Desktop/Document'
walk = os.walk(path)
index_file = open(path + '/' + 'index.txt')
index = int(index_file.read())
index_file.close()

doc_paths = []
for root, dirs, files in walk:
    there_is_any_img = False
    for curr_file in files:
        if curr_file.endswith(".png"):
            there_is_any_img = True

    if there_is_any_img:
        root = root.replace("\\", "/")
        doc_paths.append(root)

doc_win = win_pygame.WinPygame(doc_paths, index)

while 1:
    doc_win.main_loop()
    doc_win.control_panel.root.update()
    doc_win.control_panel.root.update_idletasks()

# TODO: Actualmente sólo se muestra la primera imagen de cada documento.
    # Añadir control que permita navegar entre imágenes

# TODO: Al añadir un sello nuevo, este no se carga en la lista hasta q se resetea el programa.
# TODO: Al añadir un sello nuevo, el documento no se clasifica automáticamente con dicho sello y hay que volver a hacerlo
