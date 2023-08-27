import pygame

from constants.sizes import SCREEN_HEIGHT, SCREEN_WIDTH
from constants.texts import YOUR_SCORE_IS_TEXT


# single responsibility / open closed


def your_score_is(screen, score):
    font = pygame.font.Font(None, 37)
    text = font.render(YOUR_SCORE_IS_TEXT + str(score), True, (255, 255, 255))
    screen.blit(text, (SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 2 - 40))

