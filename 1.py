print("Encryption\n")
def encrypt(text,s):
	result = ""
	for i in range(len(text)):
		char = text[i]
		if (char.isupper()):
			result += chr((ord(char) + s-65) % 26 + 65)
		else:
			result += chr((ord(char) + s - 97) % 26 + 97)
	return result
text = "kaifmunhsi"
s = 3
print(f'Text: {text}')
print(f'Shift: {s}')
print(f'Cipher Text: {encrypt(text,s)}')

print("Decrpytion\n")

def decrypt(cipher, s):
	 result = ""
	 for i in range(len(cipher)):
	 	char = cipher[i]
	 	if char.isupper():
	 		result += chr((ord(char) - s - 65) % 26 + 65)
	 	else:
			 result += chr((ord(char) - s - 97) % 26 + 97)
	 return result
cipher = "ndlipxqkvl"
s = 3
print(f'Text: {cipher}')
print(f'Shift: {s}')
print(f'Decrypt Text: {decrypt(cipher,s)}')