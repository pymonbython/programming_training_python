import subprocess
import time
import os

from pynput import keyboard

controller = keyboard.Controller()
pressed = [keyboard.Key.cmd_l, 'd']
# controller.press(keyboard.Key.esc)
# with controller.pressed(*pressed):
    # time.sleep(5)
    # controller.press('d')
    # controller.type('firefox')
# controller.press(keyboard.Key.cmd)
# time.sleep(5)
# controller.press('d')
# os.system("xdotool key Super+d &")
# time.sleep(5)
time.sleep(.1)
subprocess.Popen(["xdotool", "key", "Super+Left"])
subprocess.Popen(["xdotool", "key", "Super+d"])
time.sleep(1)
subprocess.Popen(["xdotool", "type", "firefox"])
time.sleep(1)
controller.press(keyboard.Key.enter)
controller.release(keyboard.Key.enter)
time.sleep(1)
with controller.pressed(keyboard.Key.ctrl_l):
    controller.press('t')
    controller.release('t')
    time.sleep(1)
    controller.press('l')
    # controller.release('l')

controller.type('https://app.slack.com/client/T0L9S2U6Q')
time.sleep(.1)
controller.press(keyboard.Key.enter)
controller.release(keyboard.Key.enter)
time.sleep(10)
controller.press(keyboard.Key.esc)
controller.release(keyboard.Key.esc)
# os.system('xdotool type "firefox"')


# time.sleep(0.5)  # Opcjonalne opóźnienie
# controller.press(keyboard.Key.cmd)  # Super (Cmd)
# controller.press('d')
# controller.release('d')
# controller.release(keyboard.Key.cmd)



# controller.release('d')
# controller.release(keyboard.Key.cmd)

# controller.type('firefox')
# controller.press()


# 1. Wciskamy cmd/start + d
# 2. Wpisuję słowo firefox
# 3. Wciskam enter