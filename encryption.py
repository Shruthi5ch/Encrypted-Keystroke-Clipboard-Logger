from cryptography.fernet import Fernet

def generate_key():
    with open("secret", "wb") as f:
        f.write(Fernet.generate_key())

def load_key():
    with open("secret", "rb") as f:
        return f.read()

def encrypt_data(data: str, key: bytes) -> str:
    return Fernet(key).encrypt(data.encode()).decode()

def decrypt_data(token: str, key: bytes) -> str:
    return Fernet(key).decrypt(token.encode()).decode()
