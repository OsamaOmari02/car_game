import pygame.font


def score_counter(screen, score):
    font = pygame.font.Font(None, 40)
    score = font.render("Score: " + str(score), True, (255, 255, 255))
    screen.blit(score, (5, 40))
