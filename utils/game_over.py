import time

import pygame

from constants.other import *
from constants.sizes import MY_CAR_WIDTH, SCREEN_WIDTH, SCREEN_HEIGHT
from constants.sounds import GAME_OVER_SOUND
from constants.texts import GAME_OVER_TEXT
from utils.your_score_is import your_score_is


def game_over(screen, score, is_insane_mode=False):
    GAME_OVER_SOUND.play()
    font = pygame.font.Font(None, 70)
    text = font.render(GAME_OVER_TEXT, True, (255, 0, 0))
    screen.blit(text, (SCREEN_WIDTH // 2 - 150, SCREEN_HEIGHT // 2 - 100))
    your_score_is(screen, score)
    pygame.display.update()
    time.sleep(4)
    if is_insane_mode:
        return 3, 0, ENEMY_CAR_Y, (SCREEN_WIDTH - MY_CAR_WIDTH) // 2, INSANE_ENEMY_CAR_SPEED
    return 3, 0, ENEMY_CAR_Y, (SCREEN_WIDTH - MY_CAR_WIDTH) // 2, NORMAL_ENEMY_CAR_SPEED

