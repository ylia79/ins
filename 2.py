import string

def encrypt(text, key):
    alphabet = string.ascii_lowercase
    encrypted_text = ""
    for char in text.lower():
        if char in alphabet:
            index = alphabet.index(char)
            encrypted_text += key[index]
        else:
            encrypted_text += char
    return encrypted_text

def decrypt(encrypted_text, key):
    alphabet = string.ascii_lowercase
    decrypted_text = ""
    for char in encrypted_text.lower():
        if char in key:
            index = key.index(char)
            decrypted_text += alphabet[index]
        else:
            decrypted_text += char
    return decrypted_text

text = "kaifmunshi"
key = "abcdefghjklmnopqrstuvwxyz"
cipher_text = encrypt(text, key)
print("Cipher Text:", cipher_text)
decrypted_text = decrypt(cipher_text, key)
print("Decrypted Text:", decrypted_text)
