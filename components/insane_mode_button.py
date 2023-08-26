import pygame
from constants.sizes import *  # Import your size constants here


def insane_mode_button_comp():
    font = pygame.font.Font(None, 30)
    button_text = font.render("Insane Mode", True, (255, 255, 255))
    button = pygame.Surface((button_width-10, button_height-10), pygame.SRCALPHA)  # Use SRCALPHA for transparency

    # Create a gradient background for the button
    for y in range(button_height):
        alpha = int(255 * (1 - y / button_height))  # Create a vertical gradient
        pygame.draw.line(button, (255, 0, 0, alpha), (0, y), (button_width, y))  # Green gradient color

    # Draw a border around the button
    pygame.draw.rect(button, (255, 255, 255), button.get_rect(), 2)

    # Blit the text onto the button surface
    button.blit(
        button_text, button_text.get_rect(center=(button_width // 2, button_height // 2)).topleft
    )

    # Calculate button position to the left of the "Start" button
    button_rect = button.get_rect(center=(width // 2 + (button_width + button_spacing), height - button_height // 2 - 20))
    return button, button_rect
