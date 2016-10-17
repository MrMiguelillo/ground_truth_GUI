import sys
import pygame
from pygame_functions import PygameFunctions as pf


def calc_rect(coords):
    minx = min(coords[0], coords[2])
    maxx = max(coords[0], coords[2])
    miny = min(coords[1], coords[3])
    maxy = max(coords[1], coords[3])

    return minx, miny, maxx, maxy

pygame.init()

size = width, height = 1200, 650
speed = [1, 1]
black = 0, 0, 0

screen = pygame.display.set_mode(size)

doc_img = pygame.image.load(r"C:\Users\usuario\Desktop\document\1823-L119.M3\117\IMG_0001.png")
img_c = doc_img.copy()

scale = 1
originx, originy = (0, 0)
pt1x, pt1y = (0, 0)
pt2x, pt2y = (0, 0)
movement_speed = 10
clock = pygame.time.Clock()

image = pygame.transform.scale(img_c, (int(doc_img.get_width() * scale), int(doc_img.get_height() * scale)))

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYUP and event.key == pygame.K_ESCAPE):
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1 or event.button == 3:
                pf.clear_old_rect(img_c, doc_img, (pt1x, pt1y, pt2x, pt2y), event.button)
                mouse_coords = pygame.mouse.get_pos()
                pt1x, pt1y, pt2x, pt2y = \
                    pf.draw_new_rect((pt1x, pt1y, pt2x, pt2y), img_c, (originx, originy),
                                     scale, mouse_coords, event.button)
            if event.button == 4 or event.button == 5:
                scale = pf.scale_img(scale, event.button)

    originx, originy = pf.move_image(originx, originy)

    image = pygame.transform.scale(img_c, (int(img_c.get_width() * scale), int(img_c.get_height() * scale)))

    screen.fill(black)
    screen.blit(image, (originx, originy))
    pygame.display.flip()

    clock.tick(60)

# TODO: Edit program to use functions
