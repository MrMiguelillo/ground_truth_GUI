import sys
import pygame


def calc_rect(coords):
    minx = min(coords[0], coords[2])
    maxx = max(coords[0], coords[2])
    miny = min(coords[1], coords[3])
    maxy = max(coords[1], coords[3])

    return minx, miny, maxx, maxy

pygame.init()

size = width, height = 600, 400
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
            if event.button == 1:
                rect_coords = calc_rect((pt1x, pt1y, pt2x, pt2y))
                img_c.blit(doc_img, (rect_coords[0]-5, rect_coords[1]-5), area=(rect_coords[0]-5,
                                                                                rect_coords[1]-5,
                                                                                rect_coords[2]+5,
                                                                                rect_coords[3]+5))
                pygame.draw.circle(img_c, (0, 0, 255), (pt2x, pt2y), 5)
                temp_coords = pygame.mouse.get_pos()
                pt1x, pt1y = (int((temp_coords[0] - originx)/scale), int((temp_coords[1] - originy)/scale))
                pygame.draw.circle(img_c, (255, 0, 0), (pt1x, pt1y), 5)
                rect_coords = calc_rect((pt1x, pt1y, pt2x, pt2y))
                pygame.draw.rect(img_c, (0, 255, 0), (pt1x, pt1y, pt2x-pt1x, pt2y-pt1y), 3)
            if event.button == 3:
                rect_coords = calc_rect((pt1x, pt1y, pt2x, pt2y))
                img_c.blit(doc_img, (rect_coords[0] - 5, rect_coords[1] - 5), area=(rect_coords[0] - 5,
                                                                                    rect_coords[1] - 5,
                                                                                    rect_coords[2] + 5,
                                                                                    rect_coords[3] + 5))
                pygame.draw.circle(img_c, (255, 0, 0), (pt1x, pt1y), 5)
                temp_coords = pygame.mouse.get_pos()
                pt2x, pt2y = (int((temp_coords[0] - originx)/scale), int((temp_coords[1] - originy)/scale))
                pygame.draw.circle(img_c, (0, 0, 255), (pt2x, pt2y), 5)
                rect_coords = calc_rect((pt1x, pt1y, pt2x, pt2y))
                pygame.draw.rect(img_c, (0, 255, 0), (pt2x, pt2y, pt1x-pt2x, pt1y-pt2y), 3)
            if event.button == 4:
                scale += 0.05
            elif event.button == 5 and scale > 0:
                scale -= 0.05

    if pygame.key.get_pressed()[pygame.K_LEFT] != 0:
        originx -= movement_speed
    elif pygame.key.get_pressed()[pygame.K_RIGHT] != 0:
        originx += movement_speed
    if pygame.key.get_pressed()[pygame.K_UP] != 0:
        originy -= movement_speed
    elif pygame.key.get_pressed()[pygame.K_DOWN] != 0:
        originy += movement_speed

    image = pygame.transform.scale(img_c, (int(img_c.get_width() * scale), int(img_c.get_height() * scale)))

    screen.fill(black)
    screen.blit(image, (originx, originy))
    pygame.display.flip()

    clock.tick(60)

# TODO: Known bug fully or partially deletes circles from the opposite color sometimes
