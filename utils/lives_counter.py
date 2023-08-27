from constants.images import LIFE_HEART_IMAGE
from constants.sizes import LIFE_HEART_WIDTH


def lives_counter(screen, lives):
    position = 0
    for _ in range(lives):
        screen.blit(LIFE_HEART_IMAGE, (1100 + position, 30))
        position -= LIFE_HEART_WIDTH

