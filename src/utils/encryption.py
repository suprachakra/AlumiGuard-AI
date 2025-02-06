from cryptography.fernet import Fernet

def encrypt_weights(weights):
    key = Fernet.generate_key()
    f = Fernet(key)
    encrypted_weights = f.encrypt(weights)
    return encrypted_weights, key

def decrypt_weights(encrypted_weights, key):
    f = Fernet(key)
    return f.decrypt(encrypted_weights)
