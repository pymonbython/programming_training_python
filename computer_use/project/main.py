import subprocess
import time
import os

from pynput import keyboard, mouse


class Controller:
    """Control mouse and keyboard."""
    def __init__(self) -> None:
        self.mouse = mouse.Controller()
        self.keyboard = keyboard.Controller()
        self.d_menu = subprocess.Popen

    # @with_sleep
    def click_button(self, button):
        self.keyboard.press(button)
        self.keyboard.release(button)
        time.sleep(.1)

    def control_d_menu(self, action, payload):
        self.d_menu(['zdotool', action, payload])
        time.sleep(.1)

    def type(self, text):
        self.keyboard.type(text)
        time.sleep(.1)

    def click_with_pressed_button(self, with_buttons: list, buttons: list):
        with self.keyboard.pressed(*with_buttons):
            for n_button in len(buttons):
                if n_button == len(buttons) - 1:
                    break
                self.click_button(buttons[n_button])
                time.sleep(.1)

            self.keyboard.press(buttons[-1])
            time.sleep(.1)


# Only one window on 34" monitor.
SLACK_PL_AUTOBOLD_CHANNEL = (178, 438)
SLACK_NEW_MESSAGE_TEXT_AREA = (922, 1326)
URL_ADDRESS = 'https://app.slack.com/client/T0L9S2U6Q'
MESSAGE_FROM_AI = 'Hej! Z tej strony Boten Anna, przejęłam kontrolę nad systemem Szymuraia, mojego feudalnego pana!'

def main():
    controller = Controller()
    # Otwieramy firefox z poziomu d-menu w i3wm/Ubuntu za pomocą narzędzia xdotool połączonego w subprocesie.
    controller.control_d_menu('key', 'Super+Left')
    controller.control_d_menu('key', 'Super+d')
    controller.control_d_menu('type', 'firefox')
    time.sleep(.9)
    controller.click(keyboard.Key.enter)
    time.sleep(.9)

    # Otwieramy nową zakładkę i wpisujemy zadeklarowany adres URL.
    controller.click_with_pressed_button([keyboard.Key.ctrl_l], ['t', 'l'])
    controller.type(URL_ADDRESS)
    controller.click_button(keyboard.Key.enter)

    # Czekamy na wczytanie się app.slack, a następnie klikamy "OK" na popupie.
    time.sleep(10)
    keyboard_controller.press(keyboard.Key.esc)
    keyboard_controller.release(keyboard.Key.esc)
    time.sleep(.1)

    # Otwieramy zadeklarowany kanał Slack, a następnie robimy focus na okienku nowej wiadomości.
    mouse_controller.position = SLACK_PL_AUTOBOLD_CHANNEL
    mouse_controller.click(mouse.Button.left)
    time.sleep(.1)
    mouse_controller.position = SLACK_NEW_MESSAGE_TEXT_AREA
    mouse_controller.click(mouse.Button.left)
    time.sleep(.1)
    keyboard_controller.type(MESSAGE_FROM_AI)
    time.sleep(.1)
    keyboard_controller.press(keyboard.Key.enter)
    keyboard_controller.release(keyboard.Key.enter)
    time.sleep(.1)

    keyboard_controller.type()

if __name__ == '__main__':
    main()
