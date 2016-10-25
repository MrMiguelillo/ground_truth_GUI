import os
import sys
import pygame
from pygame_functions import PygameFunctions as pf
import win_tkinter


class WinPygame:
    def __init__(self, path=None):
        self.size = self.width, self.height = 1200, 650
        self.speed = [1, 1]
        self.black = 0, 0, 0

        pygame.init()
        
        self.screen = pygame.display.set_mode(self.size)

        if path is not None:
            onlyimages = [f for f in os.listdir(path[0])
                          if os.path.isfile(os.path.join(path[0], f)) and f.endswith('.png')]
            self.doc_img = pygame.image.load(path[0] + '/' + onlyimages[0])
        else:
            self.doc_img = pygame.image.load(r"C:\Users\usuario\Desktop\document\1823-L119.M3\117\IMG_0001.png")

        self.img_c = self.doc_img.copy()

        self.scale = 1
        self.originx, self.originy = (0, 0)
        self.pt1x, self.pt1y = (0, 0)
        self.pt2x, self.pt2y = (0, 0)
        self.movement_speed = 10
        self.clock = pygame.time.Clock()

        self.image = pygame.transform.scale(self.img_c, (int(self.doc_img.get_width() * self.scale),
                                                         int(self.doc_img.get_height() * self.scale)))

        if __name__ != "__main__":
            self.control_panel = win_tkinter.WinControlPanel(self, (self.pt1x, self.pt1y, self.pt2x, self.pt2y), path)

    def main_loop(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYUP and event.key == pygame.K_ESCAPE):
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1 or event.button == 3:
                    pf.clear_old_rect(self.img_c, self.doc_img, (self.pt1x, self.pt1y, self.pt2x, self.pt2y), event.button)
                    mouse_coords = pygame.mouse.get_pos()
                    self.pt1x, self.pt1y, self.pt2x, self.pt2y = \
                        pf.draw_new_rect((self.pt1x, self.pt1y, self.pt2x, self.pt2y), self.img_c, (self.originx, self.originy),
                                         self.scale, mouse_coords, event.button)
                    if __name__ != "__main__":
                        self.control_panel.update_labels((self.pt1x, self.pt1y, self.pt2x, self.pt2y))

                if event.button == 4 or event.button == 5:
                    self.scale = pf.scale_img(self.scale, event.button)

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

if __name__ == "__main__":
    win = WinPygame()
    while 1:
        win.main_loop()

# TODO: Turn pt1 and pt2 lists instead
