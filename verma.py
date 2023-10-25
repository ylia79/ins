import random

def generate_random_key(length):
    key = ''.join(random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ ') for _ in range(length))
    return key

def vernam_cipher_encrypt(plaintext, key):
    if len(plaintext) != len(key):
        raise ValueError("Plaintext and key must have the same length.")
    ciphertext = ''.join(chr(ord(plaintext[i]) ^ ord(key[i])) for i in range(len(plaintext)))
    return ciphertext

def vernam_cipher_decrypt(ciphertext, key):
    if len(ciphertext) != len(key):
        raise ValueError("Ciphertext and key must have the same length.")
    plaintext = ''.join(chr(ord(ciphertext[i]) ^ ord(key[i])) for i in range(len(ciphertext)))
    return plaintext

plaintext = ""
key = generate_random_key(len(plaintext))
encrypted_text = vernam_cipher_encrypt(plaintext, key)
decrypted_text = vernam_cipher_decrypt(encrypted_text, key)

print("Plaintext:", plaintext)
print("Key:", key)
print("Encrypted Text:", encrypted_text)
print("Decrypted Text:", decrypted_text)
