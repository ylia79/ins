def columnar_cipher_encrypt(plaintext, key):
    key_order = sorted(range(len(key)), key=lambda k: key[k])
    
    num_cols = len(key)
    num_rows = -(-len(plaintext) // num_cols)
    

    padded_plaintext = plaintext + ' ' * (num_cols * num_rows - len(plaintext))
    
    columns = [padded_plaintext[i:i+num_rows] for i in range(0, len(padded_plaintext), num_rows)]
    
    ciphertext = ''.join(columns[i] for i in key_order)
    
    return ciphertext

plaintext = "Eavesdroppingbehindthewall"
key = [2, 1, 4, 3]
encrypted_text = columnar_cipher_encrypt(plaintext, key)
print("Plaintext:", plaintext)
print("Encrypted Text:", encrypted_text)

# Decryption Program
def columnar_cipher_decrypt(ciphertext, key):
    key_order = sorted(range(len(key)), key=lambda k: key[k])
    
    num_cols = len(key)
    num_rows = -(-len(ciphertext) // num_cols)
    
    columns = [ciphertext[i*num_rows:(i+1)*num_rows] for i in key_order]
    
    plaintext = ''.join(columns[i // num_rows][i % num_rows] for i in range(len(ciphertext)))
    
    return plaintext

a = input("Enter the text to decrypt: ")
decrypted_text = columnar_cipher_decrypt(a, key)
print("Decrypted Text:", decrypted_text)
