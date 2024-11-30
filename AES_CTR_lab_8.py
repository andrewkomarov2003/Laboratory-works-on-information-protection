from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
import os

def encrypt_aes_ctr(plaintext, key):
    # Випадковий nonce
    nonce = os.urandom(16)

    # Шифратор:
    cipher = Cipher(
        algorithms.AES(key),
        modes.CTR(nonce),
        backend=default_backend()
    )

    encryptor = cipher.encryptor()

    # Шифрування:
    ciphertext = encryptor.update(plaintext) + encryptor.finalize()

    return nonce + ciphertext

def decrypt_aes_ctr(ciphertext_with_nonce, key):
    # Витягуємо nonce з початку зашифрованого тексту
    nonce = ciphertext_with_nonce[:16]
    ciphertext = ciphertext_with_nonce[16:]

    # Дешифратор:
    cipher = Cipher(
        algorithms.AES(key),
        modes.CTR(nonce),
        backend=default_backend()
    )

    decryptor = cipher.decryptor()

    # Дешифрування:
    decrypted_text = decryptor.update(ciphertext) + decryptor.finalize()

    return decrypted_text

# Тестування:
key = os.urandom(32)  # 256-бітний ключ
plaintext = "Тестування реалізації AES шифрування у режимі CTR для лабораторноъ роботи 8 по Захисту даних!".encode('utf-8')

ciphertext = encrypt_aes_ctr(plaintext, key)
print("Зашифрований текст:", ciphertext)

decrypted_text = decrypt_aes_ctr(ciphertext, key)
print("Розшифрований текст:", decrypted_text.decode('utf-8'))

