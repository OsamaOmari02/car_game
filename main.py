# osama bassam omari 144832
import random

import pygame.display
from components.start_button import *
from constants.other import *
from constants.screens import *
from constants.sounds import MAIN_MENU_SCREEN_SOUND
from constants.texts import *
from screens.game_screen import game_screen
from screens.insane_mode_screen import insane_mode_screen
from screens.main_menu_screen import main_menu_screen
from services.buttons_service import ButtonsService
from utils.description_popup_util import description_popup_util
from utils.is_clicked_inside_area import is_clicked_inside_area

current_screen = MAIN_MENU_SCREEN


def main():
    pygame.init()
    # determine which screen to display
    global current_screen
    # my car position
    my_car_x = MY_CAR_X
    my_car_y = MY_CAR_Y
    # enemy car position
    enemy_car_x = random.randrange(200, 650)
    enemy_car_y = ENEMY_CAR_Y
    enemy_car_speed = NORMAL_ENEMY_CAR_SPEED
    enemy_car_speed_insane = INSANE_ENEMY_CAR_SPEED
    score = 0
    lives = 3
    # creating screen
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    # creating game title
    pygame.display.set_caption(GAME_TITLE)
    start_timer = True
    exit_game = False
    show_popup = False
    # start game
    while not exit_game:
        main_menu_screen(screen, show_popup)
        # draw the buttons
        start_button, start_button_rect = ButtonsService.start_button()
        how_to_play_button, how_to_play_button_rect = ButtonsService.how_to_play_button()
        insane_mode_button, insane_mode_button_rect = ButtonsService.insane_mode_button()
        _, ok_popup_button_rect = description_popup_util()
        screen.blit(start_button, start_button_rect.topleft)
        screen.blit(how_to_play_button, how_to_play_button_rect.topleft)
        screen.blit(insane_mode_button, insane_mode_button_rect.topleft)
        if current_screen == GAME_SCREEN:
            MAIN_MENU_SCREEN_SOUND.stop()
            score, my_car_x, my_car_y, enemy_car_x, enemy_car_y, enemy_car_speed, lives, current_screen = game_screen(
                screen, score, my_car_x, my_car_y, enemy_car_x, enemy_car_y, enemy_car_speed, lives)
        if current_screen == INSANE_MODE_SCREEN:
            MAIN_MENU_SCREEN_SOUND.stop()
            lives = 1
            score, my_car_x, my_car_y, enemy_car_x, enemy_car_y, enemy_car_speed_insane, lives, start_timer, current_screen = insane_mode_screen(
                screen, score, my_car_x, my_car_y, enemy_car_x, enemy_car_y, enemy_car_speed_insane, lives, start_timer)
        # event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_game = True
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if is_clicked_inside_area(event.pos, OK_BUTTON_AREA) and show_popup:
                    show_popup = False
                if how_to_play_button_rect.collidepoint(event.pos):
                    show_popup = True
                elif start_button_rect.collidepoint(event.pos):
                    current_screen = GAME_SCREEN  # Switch to the game screen
                elif insane_mode_button_rect.collidepoint(event.pos):
                    current_screen = INSANE_MODE_SCREEN  # Switch to the insane mode screen
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    my_car_x += 70  # my car movement distance
                if event.key == pygame.K_LEFT:
                    my_car_x += -70  # my car movement distance

        pygame.display.update()


main()
