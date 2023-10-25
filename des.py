import pyDes
import secrets

def generate_key():
    return secrets.token_bytes(8)

def des_encrypt(key, plaintext):
    des = pyDes.des(key, pyDes.ECB, padmode=pyDes.PAD_PKCS5)
    encrypted_data = des.encrypt(plaintext)
    return encrypted_data

def des_decrypt(key, ciphertext):
    des = pyDes.des(key, pyDes.ECB, padmode=pyDes.PAD_PKCS5)
    decrypted_data = des.decrypt(ciphertext)
    return decrypted_data

secret_key = generate_key()
data_to_encrypt = b''
encrypted_data = des_encrypt(secret_key, data_to_encrypt)
print(f'Key: {secret_key.hex()}')
print(f'Encrypted data: {encrypted_data.hex()}')
decrypted_data = des_decrypt(secret_key, encrypted_data)
print(f'Decrpyted data: {decrypted_data.decode()}')
