import time

import pygame

from constants.sizes import height, width
from constants.texts import CAR_CRASHED_TEXT


def car_crashed(screen):
    font = pygame.font.Font(None, 70)
    score = font.render(CAR_CRASHED_TEXT, True, (255, 0, 0))
    screen.blit(score, (width // 2 - 150, height // 2 - 100))
    pygame.display.update()
    time.sleep(1)

