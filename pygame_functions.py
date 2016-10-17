import pygame


class PygameFunctions:
    MOVEMENT_SPEED = 10

    @staticmethod
    def move_image(orx, ory):
        if pygame.key.get_pressed()[pygame.K_LEFT] != 0:
            orx += PygameFunctions.MOVEMENT_SPEED
        elif pygame.key.get_pressed()[pygame.K_RIGHT] != 0:
            orx -= PygameFunctions.MOVEMENT_SPEED
        if pygame.key.get_pressed()[pygame.K_UP] != 0:
            ory += PygameFunctions.MOVEMENT_SPEED
        elif pygame.key.get_pressed()[pygame.K_DOWN] != 0:
            ory -= PygameFunctions.MOVEMENT_SPEED

        return orx, ory

    @staticmethod
    def calc_rect(coords):
        minx = min(coords[0], coords[2])
        maxx = max(coords[0], coords[2])
        miny = min(coords[1], coords[3])
        maxy = max(coords[1], coords[3])

        return minx, miny, maxx, maxy

    @staticmethod
    def clear_old_rect(img, model_img, coords, button):
        rect_coords = PygameFunctions.calc_rect(coords)
        img.blit(model_img, (rect_coords[0] - 5, rect_coords[1] - 5), area=(rect_coords[0] - 5,
                                                                            rect_coords[1] - 5,
                                                                            rect_coords[2] - rect_coords[0] + 10,
                                                                            rect_coords[3] - rect_coords[1] + 10))
        if button == 1:
            pygame.draw.circle(img, (0, 0, 255), (coords[2], coords[3]), 5)
        elif button == 3:
            pygame.draw.circle(img, (255, 0, 0), (coords[0], coords[1]), 5)

    @staticmethod
    def draw_new_rect(coords, img, img_origin, scale, mouse_coords, button):
        newx, newy = (int((mouse_coords[0] - img_origin[0]) / scale), int((mouse_coords[1] - img_origin[1]) / scale))
        if button == 1:
            pygame.draw.circle(img, (255, 0, 0), (newx, newy), 5)
            pygame.draw.rect(img, (0, 255, 0), (newx, newy, coords[2] - newx, coords[3] - newy), 3)
            new_coords = (newx, newy, coords[2], coords[3])
        elif button == 3:
            pygame.draw.circle(img, (0, 0, 255), (newx, newy), 5)
            pygame.draw.rect(img, (0, 255, 0), (newx, newy, coords[0] - newx, coords[1] - newy), 3)
            new_coords = (coords[0], coords[1], newx, newy)

        return new_coords
