import pygame.font

from constants.texts import SCORE


def score_counter(screen, score):
    font = pygame.font.Font(None, 40)
    score = font.render(SCORE + str(score), True, (255, 255, 255))
    screen.blit(score, (5, 40))
