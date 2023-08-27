# creating background image
import pygame

from constants.sizes import *

MAIN_MENU_SCREEN_BACKGROUND_IMAGE = pygame.image.load("/Users/my/PycharmProjects/speed4speed/assets/images/home_background.jpeg")
MAIN_MENU_SCREEN_BACKGROUND_IMAGE = pygame.transform.scale(MAIN_MENU_SCREEN_BACKGROUND_IMAGE, (SCREEN_WIDTH, SCREEN_HEIGHT))

GAME_SCREEN_BACKGROUND_IMAGE = pygame.image.load("/Users/my/PycharmProjects/speed4speed/assets/images/game_background.png")
GAME_SCREEN_BACKGROUND_IMAGE = pygame.transform.scale(GAME_SCREEN_BACKGROUND_IMAGE, (SCREEN_WIDTH, SCREEN_HEIGHT))

MY_CAR_IMAGE = pygame.image.load("/Users/my/PycharmProjects/speed4speed/assets/images/my_car.png")
MY_CAR_IMAGE = pygame.transform.scale(MY_CAR_IMAGE, (MY_CAR_WIDTH, MY_CAR_HEIGHT))

ENEMY_CAR_IMAGE = pygame.image.load("/Users/my/PycharmProjects/speed4speed/assets/images/enemy_car.png")
ENEMY_CAR_IMAGE = pygame.transform.scale(ENEMY_CAR_IMAGE, (ENEMY_CAR_WIDTH, ENEMY_CAR_HEIGHT))

LIFE_HEART_IMAGE = pygame.image.load("/Users/my/PycharmProjects/speed4speed/assets/images/life_heart.png")
LIFE_HEART_IMAGE = pygame.transform.scale(LIFE_HEART_IMAGE, (LIFE_HEART_WIDTH, LIFE_HEART_HEIGHT))
