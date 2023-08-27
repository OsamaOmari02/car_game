import pygame

from constants.sizes import width, height
from constants.texts import YOUR_SCORE_IS_TEXT


# single responsibility / open closed


def your_score_is(screen, score):
    font = pygame.font.Font(None, 35)
    text = font.render(YOUR_SCORE_IS_TEXT + str(score), True, (255, 255, 255))
    screen.blit(text, (width // 2 - 150, height // 2 + 400))

