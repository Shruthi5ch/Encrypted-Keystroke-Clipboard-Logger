#  🔐 Encrypted Keystroke & Clipboard Logger

 This Python project securely captures and logs keystrokes and clipboard data, encrypting each in separate files using a secret key stored in a dedicated key file. It includes a decryption tool that leverages this key to safely convert the encrypted logs back into separate, readable files containing the original keystrokes and clipboard contents.

### ✅ Features

- 🔑 Records all keyboard input (one keystroke per line)
- 📋 Captures clipboard contents every 60 seconds
- 🔐 Logs are encrypted using Fernet symmetric encryption
- 🗂 Keystrokes and clipboard logs are saved in separate files
- 🧵 Uses Python threading to capture keyboard and clipboard simultaneously
- 🔓 The decryption tool converts encrypted logs and stores them in separate decrypted log files.

 ### ⚙️ Installation
 
   ** Install required packages with:
   - pip install pynput pyperclip cryptography

### 🔑 Key Generation

Run the `gen_key.py` script once to generate a secret key file. This key is used for **both encryption and decryption** of the keystroke and clipboard logs.


### Ethical Considerations

1. **Respect Privacy**: Ensure that you have explicit consent from individuals before monitoring or recording their keystrokes. Unauthorized monitoring is a serious violation of privacy.

2. **Legal Compliance**: Use this code in accordance with all applicable laws and regulations. Be aware that unauthorized use of keylogging software may be illegal in many jurisdictions.

3. **Educational Use Only**: This code is meant for learning and research purposes. It should not be used for any form of unauthorized data collection or surveillance.

4. **Responsible Use**: Do not use this code for malicious purposes. 
