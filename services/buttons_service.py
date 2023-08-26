from components.how_to_play_button import how_to_play_button_comp
from components.insane_mode_button import insane_mode_button_comp
from components.start_button import start_button_comp


class ButtonsService:
    @staticmethod
    def how_to_play_button():
        return how_to_play_button_comp()
    @staticmethod
    def start_button():
        return start_button_comp()
    @staticmethod
    def insane_mode_button():
        return insane_mode_button_comp()
