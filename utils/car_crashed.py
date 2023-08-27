import random
import time

import pygame

from constants.other import ENEMY_CAR_Y
from constants.sizes import MY_CAR_WIDTH, SCREEN_HEIGHT, SCREEN_WIDTH
from constants.sounds import CAR_CRASH_SOUND
from constants.texts import CAR_CRASHED_TEXT


def car_crashed(screen):
    CAR_CRASH_SOUND.play()
    font = pygame.font.Font(None, 70)
    score = font.render(CAR_CRASHED_TEXT, True, (255, 0, 0))
    screen.blit(score, (SCREEN_WIDTH // 2 - 150, SCREEN_HEIGHT // 2 - 100))
    pygame.display.update()
    time.sleep(1.5)
    return (SCREEN_WIDTH - MY_CAR_WIDTH) // 2, ENEMY_CAR_Y, random.randrange(200, 650)

