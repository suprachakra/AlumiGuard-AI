"""
encryption.py
-------------
Module for encrypting and decrypting sensitive information.
Utilizes the cryptography library to secure secrets.
"""

from cryptography.fernet import Fernet
from src.utils.logger import get_logger

logger = get_logger(__name__)

def generate_key():
    """Generate a new encryption key."""
    key = Fernet.generate_key()
    logger.info("New encryption key generated.")
    return key

def encrypt_data(data: bytes, key: bytes) -> bytes:
    """Encrypt data using the provided key."""
    f = Fernet(key)
    encrypted = f.encrypt(data)
    logger.debug("Data encrypted.")
    return encrypted

def decrypt_data(token: bytes, key: bytes) -> bytes:
    """Decrypt data using the provided key."""
    f = Fernet(key)
    decrypted = f.decrypt(token)
    logger.debug("Data decrypted.")
    return decrypted

if __name__ == "__main__":
    key = generate_key()
    sample_data = b"Sensitive Information"
    encrypted = encrypt_data(sample_data, key)
    decrypted = decrypt_data(encrypted, key)
    logger.info(f"Decrypted data: {decrypted.decode()}")
