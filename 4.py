def rail_fence_encrypt(plain_text, rails):
    fence = [[] for _ in range(rails)]
    rail = 0
    direction = 1
    for char in plain_text:
        fence[rail].append(char)
        rail += direction

        if rail == rails - 1 or rail == 0:
            direction *= -1

    cipher_text = ''
    for rail in fence:
        cipher_text += ''.join(rail)

    return cipher_text

def rail_fence_decrypt(cipher_text, rails):

    fence = [[] for _ in range(rails)]
    rail = 0
    direction = 1

    for char in cipher_text:
        fence[rail].append(None)
        rail += direction

        if rail == rails - 1 or rail == 0:
            direction *= -1

    index = 0


    for rail in fence:
        for i in range(len(rail)):
            rail[i] = cipher_text[index]
            index += 1

    plain_text = ''
    rail = 0
    direction = 1


    for _ in range(len(cipher_text)):
        plain_text += fence[rail].pop(0)
        rail += direction


        if rail == rails - 1 or rail == 0:
            direction *= -1

    return plain_text

plain_text = "Kaif Shaikh"
rails = 3

cipher_text = rail_fence_encrypt(plain_text, rails)
print("Cipher Text:", cipher_text)

decrypted_text = rail_fence_decrypt(cipher_text, rails)
print("Decrypted Text:", decrypted_text)
