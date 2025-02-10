from pynput import mouse, keyboard

def on_click(x, y, button, pressed):
    print(f'x = {x}, y = {y}')
    print(pressed)
    print(button)

def on_press(keyCode):
    print(keyCode)


if __name__ == '__main__':
    with mouse.Listener(on_click=on_click) as listener:
        listener.join()

    # with keyboard.Listener(on_press=on_press) as listener:
    #     listener.join()
