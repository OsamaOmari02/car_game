import time

import pygame

from constants.sizes import width, height
from constants.texts import GAME_OVER_TEXT


def game_over(screen):
    font = pygame.font.Font(None, 70)
    text = font.render(GAME_OVER_TEXT, True, (255, 0, 0))
    screen.blit(text, (width // 2 - 150, height // 2 - 100))
