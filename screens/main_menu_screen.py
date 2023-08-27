import pygame

from constants.images import MAIN_MENU_SCREEN_BACKGROUND_IMAGE
from constants.sizes import *
from constants.sounds import MAIN_MENU_SCREEN_SOUND
from constants.texts import GAME_TITLE
from utils.description_popup_util import description_popup_util


def main_menu_screen(screen, show_popup):
    if not pygame.mixer.get_busy():
        MAIN_MENU_SCREEN_SOUND.play()
    screen.blit(MAIN_MENU_SCREEN_BACKGROUND_IMAGE, dest=POSITION)
    font = pygame.font.Font(None, 80)
    text_surface = font.render(GAME_TITLE, True, (255, 255, 255))
    text_rect = text_surface.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 200))
    screen.blit(text_surface, text_rect.topleft)
    if show_popup:
        popup_surface, ok_button_rect = description_popup_util()
        popup_rect = popup_surface.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
        screen.blit(popup_surface, popup_rect.topleft)
