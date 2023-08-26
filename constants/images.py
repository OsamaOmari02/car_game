# creating background image
import pygame

from constants.sizes import *

main_menu_screen_background_image = pygame.image.load("/Users/my/PycharmProjects/speed4speed/assets/images/home_background.jpeg")
main_menu_screen_background_image = pygame.transform.scale(main_menu_screen_background_image, (width, height))

game_screen_background_image = pygame.image.load("/Users/my/PycharmProjects/speed4speed/assets/images/game_background.png")
game_screen_background_image = pygame.transform.scale(game_screen_background_image, (width, height))

my_car_image = pygame.image.load("/Users/my/PycharmProjects/speed4speed/assets/images/my_car.png")
my_car_image = pygame.transform.scale(my_car_image, (my_car_width, my_car_height))
