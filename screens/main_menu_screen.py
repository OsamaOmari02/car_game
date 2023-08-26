from constants.images import main_menu_screen_background_image
from constants.sizes import *
from utils.popup_util import description_popup_util


def main_menu_screen(screen, show_popup):
    screen.blit(main_menu_screen_background_image, dest=position)
    popup_surface, ok_button_rect = description_popup_util()
    if show_popup:
        # Draw the pop-up window
        popup_rect = popup_surface.get_rect(center=(width // 2, height // 2))
        screen.blit(popup_surface, popup_rect.topleft)
