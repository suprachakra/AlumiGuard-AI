from cryptography.fernet import Fernet

def encrypt_weights(weights):
    """
    Encrypts model weights using Fernet.
    Returns (encrypted_weights, encryption_key).
    """
    key = Fernet.generate_key()
    f = Fernet(key)
    encrypted = f.encrypt(weights)
    return encrypted, key

def decrypt_weights(encrypted_weights, key):
    """
    Decrypts model weights using the provided key.
    """
    f = Fernet(key)
    return f.decrypt(encrypted_weights)
