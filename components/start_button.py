import pygame

from constants.sizes import *
from constants.texts import START


def start_button_comp():
    font = pygame.font.Font(None, 36)
    button_text = font.render(START, True, (255, 255, 255))
    button = pygame.Surface((BUTTON_WIDTH, BUTTON_HEIGHT))
    button.fill((255, 0, 0))
    # Create a gradient background for the button
    button.fill((0, 0, 0, 0))  # Transparent background
    for y in range(BUTTON_HEIGHT):
        alpha = int(255 * (1 - y / BUTTON_HEIGHT))
        pygame.draw.line(button, (0, 0, 255, alpha), (0, y), (BUTTON_WIDTH, y))

    # Draw a border around the button
    pygame.draw.rect(button, (255, 255, 255), button.get_rect(), 2)
    # Blit the text onto the button surface
    button.blit(
        button_text, button_text.get_rect(center=(BUTTON_WIDTH // 2, BUTTON_HEIGHT // 2)).topleft
    )
    button_rect = button.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT - BUTTON_HEIGHT // 2 - 20))
    return button, button_rect
