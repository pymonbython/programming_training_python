import subprocess
import time
import os

from pynput import keyboard, mouse


# Only one window on 34" monitor.
SLACK_PL_AUTOBOLD_CHANNEL = (178, 438)
SLACK_NEW_MESSAGE_TEXT_AREA = (922, 1326)
URL_ADDRESS = 'https://app.slack.com/client/T0L9S2U6Q'
MESSAGE_FROM_AI = 'Hej! Z tej strony Boten Anna, przejęłam kontrolę nad systemem Szymuraia, mojego feudalnego pana!'

keyboard_controller = keyboard.Controller()
mouse_controller = mouse.Controller()
# pressed = [keyboard.Key.cmd_l, 'd']
# with controller.pressed(*pressed):
    # time.sleep(.1)

# Otwieramy firefox z poziomu d-menu w i3wm/Ubuntu za pomocą narzędzia xdotool połączonego w subprocesie.
subprocess.Popen(["xdotool", "key", "Super+Left"])
subprocess.Popen(["xdotool", "key", "Super+d"])
time.sleep(.1)
subprocess.Popen(["xdotool", "type", "firefox"])
time.sleep(1)
keyboard_controller.press(keyboard.Key.enter)
keyboard_controller.release(keyboard.Key.enter)
time.sleep(1)

# Otwieramy nową zakładkę i wpisujemy zadeklarowany adres URL.
with keyboard_controller.pressed(keyboard.Key.ctrl_l):
    keyboard_controller.press('t')
    keyboard_controller.release('t')
    time.sleep(.1)
    keyboard_controller.press('l')
keyboard_controller.type(URL_ADDRESS)
time.sleep(.1)
keyboard_controller.press(keyboard.Key.enter)
keyboard_controller.release(keyboard.Key.enter)

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
