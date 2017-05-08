import os
import sys
import pygame
from pygame_functions import PygameFunctions as pf
import win_tkinter

from config import path_to_documents
from config import path_to_seals


class WinPygame:
    """
    Crea una instancia de la ventana de visualización de imágenes y maneja los controles de navegación.
    Crea una instancia del panel de control
    Guarda la imagen del nuevo sello en caso de que uno sea encontrado
    """
    def __init__(self, path=None, index=0):
        self.size = self.width, self.height = 1200, 650
        self.speed = [1, 1]
        self.black = 0, 0, 0

        pygame.init()
        
        self.screen = pygame.display.set_mode(self.size)

        if path is not None:
            onlyimages = [f for f in os.listdir(path[index])
                          if os.path.isfile(os.path.join(path[index], f)) and f.endswith('.png')]
            self.doc_img = pygame.image.load(path[index] + '/' + onlyimages[0])
        else:
            # Random test image just for debugging
            self.doc_img = pygame.image.load(path_to_documents + "/1823-L119.M3/117/IMG_0001.png")

        self.img_c = self.doc_img.copy()

        self.scale = 1
        self.originx, self.originy = (0, 0)
        self.pt1x, self.pt1y = (0, 0)
        self.pt2x, self.pt2y = (0, 0)
        self.movement_speed = 10
        self.clock = pygame.time.Clock()

        self.image = pygame.transform.scale(self.img_c, (int(self.doc_img.get_width() * self.scale),
                                                         int(self.doc_img.get_height() * self.scale)))

        # Only create control panel if we are not testing
        if __name__ != "__main__":
            self.control_panel =\
                win_tkinter.WinControlPanel(self, (self.pt1x, self.pt1y, self.pt2x, self.pt2y), path, index)

    def main_loop(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYUP and event.key == pygame.K_ESCAPE):
                if __name__ == "__main__":  # If there is a control panel, closing will be handled there.
                    sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1 or event.button == 3:
                    pf.clear_old_rect(self.img_c, self.doc_img, (self.pt1x, self.pt1y, self.pt2x, self.pt2y),
                                      event.button)
                    mouse_coords = pygame.mouse.get_pos()
                    self.pt1x, self.pt1y, self.pt2x, self.pt2y = \
                        pf.draw_new_rect((self.pt1x, self.pt1y, self.pt2x, self.pt2y), self.img_c,
                                         (self.originx, self.originy), self.scale, mouse_coords, event.button)
                    if __name__ != "__main__":
                        self.control_panel.update_labels((self.pt1x, self.pt1y, self.pt2x, self.pt2y))

                if event.button == 4 or event.button == 5:
                    self.scale = pf.scale_img(self.scale, event.button)

        # Transform image acording to translation and scale
        self.originx, self.originy = pf.move_image(self.originx, self.originy)
        self.image = pygame.transform.scale(self.img_c, (int(self.img_c.get_width() * self.scale),
                                                         int(self.img_c.get_height() * self.scale)))

        self.screen.fill(self.black)
        self.screen.blit(self.image, (self.originx, self.originy))
        pygame.display.flip()

        self.clock.tick(60)

    def update_img(self, path):
        self.doc_img = pygame.image.load(path)
        self.img_c = self.doc_img.copy()
        self.scale = 1
        self.originx, self.originy = (0, 0)

    def save_seal(self, name):
        width = self.pt2x - self.pt1x
        height = self.pt2y - self.pt1y
        cropped = pygame.Surface((abs(width), abs(height)))
        cropped.blit(self.doc_img, (0, 0), (self.pt1x, self.pt1y, width, height))

        pygame.image.save(cropped, path_to_seals + name + '.png')
        # TODO: Se supone que no se van a introducir dos con el mismo nombre -> probar si se sobreescriben o da error!!

if __name__ == "__main__":
    win = WinPygame()
    while 1:
        win.main_loop()

# TODO: Turn pt1 and pt2 lists instead
