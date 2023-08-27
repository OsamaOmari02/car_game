import random

from constants.images import *
from constants.screens import MAIN_MENU_SCREEN, GAME_SCREEN
from constants.sizes import *
from constants.sounds import GAME_SCREEN_SOUND
from utils.car_crashed import car_crashed
from utils.game_over import game_over
from utils.lives_counter import lives_counter
from utils.score_counter import score_counter


def game_screen(screen, score, my_car_x, my_car_y, enemy_car_x, enemy_car_y, enemy_car_speed, lives):
    if not pygame.mixer.get_busy():
        GAME_SCREEN_SOUND.play()
    enemy_car_y -= (enemy_car_speed / 4)
    # draw images
    screen.blit(GAME_SCREEN_BACKGROUND_IMAGE, dest=POSITION)
    screen.blit(MY_CAR_IMAGE, (my_car_x, my_car_y))
    screen.blit(ENEMY_CAR_IMAGE, (enemy_car_x, enemy_car_y))
    lives_counter(screen, lives)
    # increase enemy car speed
    enemy_car_y += enemy_car_speed
    # check if there is a crash
    if my_car_y < enemy_car_y + ENEMY_CAR_HEIGHT:
        # left side and right side (after or)
        # car crashed
        if enemy_car_x < my_car_x < enemy_car_x + ENEMY_CAR_WIDTH or enemy_car_x < my_car_x + MY_CAR_WIDTH < enemy_car_x + ENEMY_CAR_WIDTH:
            lives -= 1
            if lives != 0:
                GAME_SCREEN_SOUND.stop()
                my_car_x, enemy_car_y, enemy_car_x = car_crashed(screen)
            # game over lives == 0
            else:
                GAME_SCREEN_SOUND.stop()
                lives, score, enemy_car_y, my_car_x, enemy_car_speed = game_over(screen, score)
                return score, my_car_x, my_car_y, enemy_car_x, enemy_car_y, enemy_car_speed, lives, MAIN_MENU_SCREEN
    score_counter(screen, score)
    # check if car out of boundaries
    if my_car_x + MY_CAR_WIDTH < 250 or my_car_x + MY_CAR_WIDTH > 1000:
        lives -= 1
        if lives != 0:
            GAME_SCREEN_SOUND.stop()
            my_car_x, enemy_car_y, enemy_car_x = car_crashed(screen)
        # game over lives == 0
        else:
            GAME_SCREEN_SOUND.stop()
            lives, score, enemy_car_y, my_car_x, enemy_car_speed = game_over(screen, score)
            return score, my_car_x, my_car_y, enemy_car_x, enemy_car_y, enemy_car_speed, lives, MAIN_MENU_SCREEN
    # car passed
    if enemy_car_y > SCREEN_HEIGHT:
        # regenerate another enemy car
        enemy_car_y = 0 - ENEMY_CAR_HEIGHT
        enemy_car_x = random.randrange(200, 850)
        score += 10
        if score % 50 == 0:
            enemy_car_speed += 3
    return score, my_car_x, my_car_y, enemy_car_x, enemy_car_y, enemy_car_speed, lives, GAME_SCREEN
