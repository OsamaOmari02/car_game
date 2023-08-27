# osama bassam omari 144832
import random
import time

import pygame.display
from components.start_button import *
from constants.screens import *
from constants.texts import *
from screens.game_screen import game_screen
from screens.main_menu_screen import main_menu_screen
from services.buttons_service import ButtonsService
from utils.car_crashed import car_crashed
from utils.game_over import game_over
from utils.score_counter import score_counter
from utils.start_timer_util import start_timer_util
from utils.your_score_is import your_score_is


def main():
    global my_car_image_x
    global my_car_image_y
    enemy_car_x = random.randrange(200, 650)
    enemy_car_y = -700
    enemy_car_speed = 12
    score = 0
    lives = 3
    pygame.init()
    current_screen = MAIN_MENU_SCREEN
    # creating canvas/screen
    screen = pygame.display.set_mode((width, height))
    # creating title
    pygame.display.set_caption(GAME_TITLE)
    # start game
    start_timer = True
    exit_game = False
    show_popup = False
    while not exit_game:
        main_menu_screen(screen, show_popup)
        # draw the buttons
        start_button, start_button_rect = ButtonsService.start_button()
        how_to_play_button, how_to_play_button_rect = ButtonsService.how_to_play_button()
        insane_mode_button, insane_mode_button_rect = ButtonsService.insane_mode_button()
        screen.blit(start_button, start_button_rect.topleft)
        screen.blit(how_to_play_button, how_to_play_button_rect.topleft)
        screen.blit(insane_mode_button, insane_mode_button_rect.topleft)
        if current_screen == GAME_SCREEN:
            enemy_car_y -= (enemy_car_speed / 4)
            game_screen(screen, my_car_image_x, my_car_image_y, enemy_car_x, enemy_car_y, lives)
            enemy_car_y += enemy_car_speed
            if start_timer:
                for countdown_text in countdown_texts:
                    start_timer_util(screen, countdown_text)
                start_timer = False
            if my_car_image_y < enemy_car_y + ENEMY_CAR_HEIGHT:
                # left side and right side (after or)
                if enemy_car_x < my_car_image_x < enemy_car_x + ENEMY_CAR_WIDTH or enemy_car_x < my_car_image_x + MY_CAR_WIDTH < enemy_car_x + ENEMY_CAR_WIDTH:
                    lives -= 1
                    if lives != 0:
                        car_crashed(screen)
                        enemy_car_y = -700
                    else:
                        game_over(screen)
                        your_score_is(screen, score)
                        pygame.display.update()
                        time.sleep(1)
                        lives = 3
                        score = 0
                        enemy_car_y = -700
                        current_screen = MAIN_MENU_SCREEN
                        continue
            score_counter(screen, score)
            if enemy_car_y > height:
                enemy_car_y = 0 - ENEMY_CAR_HEIGHT
                enemy_car_x = random.randrange(200, 850)
                score += 10
                if score % 50 == 0:
                    enemy_car_speed += 3

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_game = True
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if how_to_play_button_rect.collidepoint(event.pos):
                    show_popup = True
                elif start_button_rect.collidepoint(event.pos):
                    current_screen = GAME_SCREEN  # Switch to the game screen
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    my_car_image_x += 70
                if event.key == pygame.K_LEFT:
                    my_car_image_x += -70

            # # pressing anywhere will dismiss the pop-up for better UX
            # else:
            #     show_popup = False  # Dismiss the pop-up
        pygame.display.update()


main()
