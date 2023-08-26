from screens.game_screen import *


def start_timer_util(screen, countdown_text):
    font = pygame.font.Font(None, 150)  # You can adjust the font size as needed
    text_rendered = font.render(countdown_text, True, (255, 255, 255))  # White text color
    text_rect = text_rendered.get_rect(center=(width // 2, height // 2))  # Center of the screen
    screen.blit(text_rendered, text_rect.topleft)
    pygame.display.update()
    pygame.time.wait(1000)  # Pause for 1 second
    screen.blit(game_screen_background_image, dest=position)
    screen.blit(my_car_image, (my_car_image_x, my_car_image_y))
    pygame.display.update()
