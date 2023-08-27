import pygame

from constants.texts import DESCRIPTION_TEXTS


def description_popup_util():
    # Create a pop-up window surface
    popup_width, popup_height = 600, 250
    popup_surface = pygame.Surface((popup_width, popup_height))
    popup_surface.fill((200, 200, 200))  # Background color
    # Define font for the pop-up text
    font = pygame.font.Font(None, 25)
    # Background color and border
    background_color = (240, 240, 240, 220)
    border_color = (100, 100, 100)
    border_width = 3
    # Draw the background with rounded corners
    pygame.draw.rect(popup_surface, background_color, (0, 0, popup_width, popup_height), border_radius=15)
    # Draw the rounded background with transparency
    pygame.draw.rect(popup_surface, (0, 0, 0, 0), (0, 0, popup_width, popup_height), border_radius=15)
    pygame.draw.rect(popup_surface, (200, 200, 200, 220), (0, 0, popup_width, popup_height), border_radius=15)
    # Draw a border around the background
    pygame.draw.rect(popup_surface, border_color, (0, 0, popup_width, popup_height), border_width, border_radius=15)
    # Render and position the text lines
    text_color = (0, 0, 0)  # Black text color
    y_position = 20  # Starting vertical position
    for line in DESCRIPTION_TEXTS:
        line_rendered = font.render(line, True, text_color)
        line_rect = line_rendered.get_rect(center=(popup_width // 2, y_position))
        popup_surface.blit(line_rendered, line_rect.topleft)
        y_position += line_rendered.get_height() + 10  # Add some spacing
    # Create "OK" button
    button_width, button_height = 100, 40
    ok_button = pygame.Surface((button_width, button_height))
    ok_button.fill((0, 150, 0))  # Green color
    # Define button border
    button_border_color = (255, 255, 255)  # White color for border
    button_border_width = 2
    # Draw border around the "OK" button
    pygame.draw.rect(ok_button, button_border_color, ok_button.get_rect(), button_border_width)
    # Position the "OK" button at the bottom center of the pop-up
    ok_button_rect = pygame.Rect((popup_width - button_width) // 2, popup_height - 60, button_width, button_height)
    # Draw the "OK" button on the pop-up surface
    popup_surface.blit(ok_button, ok_button_rect.topleft)
    # Draw the "OK" text on the button
    ok_text = font.render("OK", True, (255, 255, 255))
    ok_text_rect = ok_text.get_rect(center=ok_button_rect.center)
    popup_surface.blit(ok_text, ok_text_rect.topleft)
    return popup_surface, ok_button_rect
