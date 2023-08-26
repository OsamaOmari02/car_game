import pygame

from constants.sizes import *


def start_button_comp():
    font = pygame.font.Font(None, 36)
    button_text = font.render("Start", True, (255, 255, 255))
    button = pygame.Surface((button_width, button_height))
    button.fill((255, 0, 0))
    # Create a gradient background for the button
    button.fill((0, 0, 0, 0))  # Transparent background
    for y in range(button_height):
        alpha = int(255 * (1 - y / button_height))  # Create a vertical gradient
        pygame.draw.line(button, (0, 0, 255, alpha), (0, y), (button_width, y))

    # Draw a border around the button
    pygame.draw.rect(button, (255, 255, 255), button.get_rect(), 2)

    # Blit the text onto the button surface
    button.blit(
        button_text, button_text.get_rect(center=(button_width // 2, button_height // 2)).topleft
    )
    button_rect = button.get_rect(center=(width // 2, height - button_height // 2 - 20))
    return button, button_rect
