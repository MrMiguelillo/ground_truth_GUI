import sys
import pygame

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
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                img_c.blit(doc_img, (pt1x-5, pt1y-5), area=(pt1x-5, pt1y-5, pt1x+5, pt1y+5))
                temp_coords = pygame.mouse.get_pos()
                pt1x, pt1y = (int((temp_coords[0] - originx)/scale), int((temp_coords[1] - originy)/scale))
                pygame.draw.circle(img_c, (255, 0, 0), (pt1x, pt1y), 5)
            if event.button == 3:
                img_c.blit(doc_img, (pt2x - 5, pt2y - 5), area=(pt2x - 5, pt2y - 5, pt2x + 5, pt2y + 5))
                temp_coords = pygame.mouse.get_pos()
                pt2x, pt2y = (int((temp_coords[0] - originx)/scale), int((temp_coords[1] - originy)/scale))
                pygame.draw.circle(img_c, (0, 0, 255), (pt2x, pt2y), 5)
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

# TODO: Modify point removal so that image gets copied from min x and y to max x and y instead of just around the points
# TODO: Draw rectangle around area marked by points
# TODO: Known bug fully or partially deletes circles from the opposite color sometimes
