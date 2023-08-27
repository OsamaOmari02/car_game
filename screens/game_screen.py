from constants.images import *
from constants.sizes import *
from utils.lives_counter import lives_counter


def game_screen(screen, my_car_x, my_car_y, enemy_car_x, enemy_car_y, lives):
    screen.blit(game_screen_background_image, dest=position)
    screen.blit(my_car_image, (my_car_x, my_car_y))
    screen.blit(ENEMY_CAR_IMAGE, (enemy_car_x, enemy_car_y))
    lives_counter(screen, lives)

