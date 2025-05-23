import pyperclip
from encryption import encrypt_data, load_key

key = load_key()

def get_encrypted_clipboard():
    try:
        data = pyperclip.paste()
        return encrypt_data(data, key)
    except Exception as e:
        return encrypt_data(f"[Clipboard error: {e}]", key)

