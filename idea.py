import binascii
from cryptography.hazmat.primitives.ciphers import algorithms, base, modes
from cryptography.hazmat.primitives import padding

def encrypt_text(key, iv, plaintext):
    key = binascii.unhexlify(key)
    iv = binascii.unhexlify(iv)
    plaintext = plaintext.encode('utf-8')

    # Pad the plaintext to match IDEA's block size (64 bits)
    padder = padding.PKCS7(64).padder()
    padded_plaintext = padder.update(plaintext)
    padded_plaintext += padder.finalize()

    cipher = base.Cipher(
        algorithms.IDEA(key),
        modes.CFB(iv),
    )
    encryptor = cipher.encryptor()
    ciphertext = encryptor.update(padded_plaintext) + encryptor.finalize()
    
    return binascii.hexlify(ciphertext).decode('utf-8')

# Decryption function
def decrypt_text(key, iv, ciphertext):
    key = binascii.unhexlify(key)
    iv = binascii.unhexlify(iv)
    ciphertext = binascii.unhexlify(ciphertext)

    cipher = base.Cipher(
        algorithms.IDEA(key),
        modes.CFB(iv),
    )
    decryptor = cipher.decryptor()
    decrypted_padded_text = decryptor.update(ciphertext) + decryptor.finalize()

    # Unpad the decrypted text
    unpadder = padding.PKCS7(64).unpadder()
    decrypted_text = unpadder.update(decrypted_padded_text)
    decrypted_text += unpadder.finalize()
    
    return decrypted_text.decode('utf-8')

key = '00112233445566778899AABBCCDDEEFF'
iv = '1122334455667788'
plaintext = 'kaifmunshi'

ciphertext = encrypt_text(key, iv, plaintext)
print("Ciphertext:", ciphertext)

# Decrypt the ciphertext
decrypted_text = decrypt_text(key, iv, ciphertext)
print("Decrypted Text:", decrypted_text)


