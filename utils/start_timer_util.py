from constants.sounds import COUNTDOWN_SOUND
from screens.game_screen import *


def start_timer_util(screen, countdown_text):
    if not pygame.mixer.get_busy():
        COUNTDOWN_SOUND.play()
    font = pygame.font.Font(None, 150)
    text_rendered = font.render(countdown_text, True, (255, 255, 255))
    text_rect = text_rendered.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))  # Center of the screen
    screen.blit(text_rendered, text_rect.topleft)
    pygame.display.update()
    pygame.time.wait(1000)  # Pause for 1 second
    screen.blit(GAME_SCREEN_BACKGROUND_IMAGE, dest=POSITION)
    screen.blit(MY_CAR_IMAGE, (MY_CAR_X, MY_CAR_Y))
    pygame.display.update()
