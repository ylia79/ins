def encryption(plain_text, key):
    key = [ord(k) for k in key]  # Convert the key to a list of ASCII values
    S = list(range(256))
    i = j = 0
    cipher_text = []
    for char in plain_text:
        i = (i + 1) % 256
        j = (j + S[i]) % 256
        S[i], S[j] = S[j], S[i]
        t = (S[i] + S[j]) % 256
        k = S[t]
        cipher_text.append(ord(char) ^ k)
    return cipher_text
def decryption(cipher_text, key):
    key = [ord(k) for k in key]  # Convert the key to a list of ASCII values
    S = list(range(256))
    i = j = 0
    decrypted_text = []
    for char in cipher_text:
        i = (i + 1) % 256
        j = (j + S[i]) % 256
        S[i], S[j] = S[j], S[i]
        t = (S[i] + S[j]) % 256
        k = S[t]
        decrypted_text.append(chr(char ^ k))
    return ''.join(decrypted_text)
if __name__ == '__main__':
    plain_text = ""
    key = "101001000001"
    cipher_text = encryption(plain_text, key)
    decrypted_text = decryption(cipher_text, key)
    print("Plain text:", plain_text)
    print("Cipher text:", ''.join(["%02X" % c for c in cipher_text]))
    print("Decrypted text:", decrypted_text)
