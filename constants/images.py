# creating background image
import pygame

from constants.sizes import *

main_menu_screen_background_image = pygame.image.load("/Users/my/PycharmProjects/speed4speed/assets/images/home_background.jpeg")
main_menu_screen_background_image = pygame.transform.scale(main_menu_screen_background_image, (width, height))

game_screen_background_image = pygame.image.load("/Users/my/PycharmProjects/speed4speed/assets/images/game_background.png")
game_screen_background_image = pygame.transform.scale(game_screen_background_image, (width, height))

my_car_image = pygame.image.load("/Users/my/PycharmProjects/speed4speed/assets/images/my_car.png")
my_car_image = pygame.transform.scale(my_car_image, (MY_CAR_WIDTH, MY_CAR_HEIGHT))

ENEMY_CAR_IMAGE = pygame.image.load("/Users/my/PycharmProjects/speed4speed/assets/images/enemy_car.png")
ENEMY_CAR_IMAGE = pygame.transform.scale(ENEMY_CAR_IMAGE, (ENEMY_CAR_WIDTH, ENEMY_CAR_HEIGHT))

LIFE_HEART_IMAGE = pygame.image.load("/Users/my/PycharmProjects/speed4speed/assets/images/life_heart.png")
LIFE_HEART_IMAGE = pygame.transform.scale(LIFE_HEART_IMAGE, (LIFE_HEART_WIDTH, LIFE_HEART_HEIGHT))
