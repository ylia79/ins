def polyalphabetic_encrypt(message, key):
    encrypted_message = []
    key_length = len(key)
    key_index = 0

    for char in message:
        if char.isalpha():
            shift = ord(key[key_index].upper()) - ord('A')
            if char.isupper():
                encrypted_char = chr(((ord(char) - ord('A') + shift) % 26) + ord('A'))
            else:
                encrypted_char = chr(((ord(char) - ord('a') + shift) % 26) + ord('a'))
            key_index = (key_index + 1) % key_length
        else:
            encrypted_char = char
        encrypted_message.append(encrypted_char)

    return ''.join(encrypted_message)

plaintext = input("Enter the message to encrypt: ")
key = input("Enter the encryption key: ")
ciphertext = polyalphabetic_encrypt(plaintext, key)
print("Encrypted message:", ciphertext)

def polyalphabetic_decrypt(ciphertext, key):
    decrypted_message = []
    key_length = len(key)
    key_index = 0

    for char in ciphertext:
        if char.isalpha():
            shift = ord(key[key_index].upper()) - ord('A')
            if char.isupper():
                decrypted_char = chr(((ord(char) - ord('A') - shift) % 26) + ord('A'))
            else:
                decrypted_char = chr(((ord(char) - ord('a') - shift) % 26) + ord('a'))
            key_index = (key_index + 1) % key_length
        else:
            decrypted_char = char
        decrypted_message.append(decrypted_char)

    return ''.join(decrypted_message)

cipher = input("Enter the message to decrypt: ")
key = input("Enter the same key used to encrypt: ")
plaintext = polyalphabetic_decrypt(cipher, key)
print("Encrypted message:", plaintext)
