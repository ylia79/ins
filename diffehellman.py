from random import randint

p = 23  
g = 5

print("Value of p is:", p)
print("Value of g is:", g)

a = randint(1, p - 1)
b = randint(1, p - 1)
A = pow(g, a, p)
B = pow(g, b, p)

secret_key_A = pow(B, a, p)
secret_key_B = pow(A, b, p)
print("Alice's private key (a):", a)
print("Bob's private key (b):", b)
print("Alice's public key (A):", A)
print("Bob's public key (B):", B)
print("Shared secret key for Alice:", secret_key_A)
print("Shared secret key for Bob:", secret_key_B)
