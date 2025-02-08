from pynput import mouse

def on_click(x, y, button, pressed):
    print(f'x = {x}, y = {y}')
    print(pressed)
    print(button)


with mouse.Listener(on_click=on_click) as listener:
    listener.join()
