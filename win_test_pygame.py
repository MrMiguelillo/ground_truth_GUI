import sys
import pygame

pygame.init()

size = width, height = 600, 400
speed = [1, 1]
black = 0, 0, 0

screen = pygame.display.set_mode(size)

doc_img = pygame.image.load(r"C:\Users\usuario\Desktop\document\1823-L119.M3\117\IMG_0001.png")

scale = 1
originx, originy = (0, 0)
pt1x, pt1y = (0, 0)
pt2x, pt2y = (0, 0)
movement_speed = 10
clock = pygame.time.Clock()

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                temp_coords = pygame.mouse.get_pos()
                pt1x, pt1y = ((temp_coords[0] - originx), (temp_coords[1] - originy))
            if event.button == 3:
                temp_coords = pygame.mouse.get_pos()
                pt2x, pt2y = ((temp_coords[0] - originx), (temp_coords[1] - originy))
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

    image = pygame.transform.scale(doc_img, (int(doc_img.get_width() * scale), int(doc_img.get_height() * scale)))
    pygame.draw.circle(image, (255, 0, 0), (pt1x, pt1y), 5)
    pygame.draw.circle(image, (0, 0, 255), (pt2x, pt2y), 5)

    screen.fill(black)
    screen.blit(image, (originx, originy))
    pygame.display.flip()

    clock.tick(60)
