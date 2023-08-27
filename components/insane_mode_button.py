import pygame
from constants.sizes import *  # Import your size constants here
from constants.texts import INSANE_MODE_TEXT


def insane_mode_button_comp():
    font = pygame.font.Font(None, 30)
    button_text = font.render(INSANE_MODE_TEXT, True, (255, 255, 255))
    text_x = (BUTTON_WIDTH - button_text.get_width()) // 2
    text_y = (BUTTON_HEIGHT - button_text.get_height()) // 2
    button = pygame.Surface((BUTTON_WIDTH, BUTTON_HEIGHT), pygame.SRCALPHA)  # Use SRCALPHA for transparency
    # Create a gradient background for the button
    for y in range(BUTTON_HEIGHT):
        alpha = int(255 * (1 - y / BUTTON_HEIGHT))  # Create a vertical gradient
        pygame.draw.line(button, (255, 0, 0, alpha), (0, y), (BUTTON_WIDTH, y))  # RED gradient color
    pygame.draw.rect(button, (255, 255, 255), button.get_rect(), 2)
    # Blit the text onto the button surface
    button.blit(button_text, (text_x, text_y))
    button_rect = button.get_rect(center=(SCREEN_WIDTH // 2 + (BUTTON_WIDTH + BUTTON_SPACING), SCREEN_HEIGHT - BUTTON_HEIGHT // 2 - 20))
    return button, button_rect
