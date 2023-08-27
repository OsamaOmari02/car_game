import random

import pygame

from constants.images import ENEMY_CAR_IMAGE, GAME_SCREEN_BACKGROUND_IMAGE, MY_CAR_IMAGE
from constants.screens import MAIN_MENU_SCREEN, INSANE_MODE_SCREEN
from constants.sizes import ENEMY_CAR_HEIGHT, ENEMY_CAR_WIDTH, MY_CAR_WIDTH, SCREEN_HEIGHT, POSITION
from constants.sounds import GAME_SCREEN_SOUND
from constants.texts import COUNTDOWN_TEXT
from utils.game_over import game_over
from utils.lives_counter import lives_counter
from utils.score_counter import score_counter
from utils.start_timer_util import start_timer_util


def insane_mode_screen(screen, score, my_car_x, my_car_y, enemy_car_x, enemy_car_y, enemy_car_speed_insane, lives, start_timer):
    enemy_car_y -= (enemy_car_speed_insane / 4)
    screen.blit(GAME_SCREEN_BACKGROUND_IMAGE, dest=POSITION)
    screen.blit(MY_CAR_IMAGE, (my_car_x, my_car_y))
    screen.blit(ENEMY_CAR_IMAGE, (enemy_car_x, enemy_car_y))
    lives_counter(screen, lives)
    enemy_car_y += enemy_car_speed_insane
    if start_timer:
        for countdown_text in COUNTDOWN_TEXT:
            start_timer_util(screen, countdown_text)
        start_timer = False
    if not pygame.mixer.get_busy():
        GAME_SCREEN_SOUND.play()
    if my_car_y < enemy_car_y + ENEMY_CAR_HEIGHT:
        # left side and right side (after or)
        if enemy_car_x < my_car_x < enemy_car_x + ENEMY_CAR_WIDTH or enemy_car_x < my_car_x + MY_CAR_WIDTH < enemy_car_x + ENEMY_CAR_WIDTH:
            GAME_SCREEN_SOUND.stop()
            lives, score, enemy_car_y, my_car_x, enemy_car_speed_insane = game_over(screen, score, True)
            return score, my_car_x, my_car_y, enemy_car_x, enemy_car_y, enemy_car_speed_insane, lives, True, MAIN_MENU_SCREEN
    score_counter(screen, score)
    if my_car_x + MY_CAR_WIDTH < 250 or my_car_x + MY_CAR_WIDTH > 1000:
        GAME_SCREEN_SOUND.stop()
        lives, score, enemy_car_y, my_car_x, enemy_car_speed_insane = game_over(screen, score, True)
        return score, my_car_x, my_car_y, enemy_car_x, enemy_car_y, enemy_car_speed_insane, lives, True, MAIN_MENU_SCREEN
    if enemy_car_y > SCREEN_HEIGHT:
        enemy_car_y = 0 - ENEMY_CAR_HEIGHT
        enemy_car_x = random.randrange(200, 850)
        score += 10
        if score % 50 == 0:
            enemy_car_speed_insane += 7
    return score, my_car_x, my_car_y, enemy_car_x, enemy_car_y, enemy_car_speed_insane, lives, start_timer, INSANE_MODE_SCREEN
