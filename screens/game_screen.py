from constants.images import *
from constants.sizes import *


def game_screen(screen, x, y):
    screen.blit(game_screen_background_image, dest=position)
    screen.blit(my_car_image, (x, y))
