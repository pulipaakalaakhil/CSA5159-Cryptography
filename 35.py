import random

plaintext = input("Enter plaintext: ").upper()

key = [random.randint(0, 25) for _ in range(len(plaintext))]

ciphertext = ""

for i in range(len(plaintext)):
    if plaintext[i].isalpha():
        p = ord(plaintext[i]) - ord('A')
        c = (p + key[i]) % 26
        ciphertext += chr(c + ord('A'))
    else:
        ciphertext += plaintext[i]

print("Random Key Stream:")
print(key)

print("Ciphertext:")
print(ciphertext)

# Decryption
decrypted = ""

for i in range(len(ciphertext)):
    if ciphertext[i].isalpha():
        c = ord(ciphertext[i]) - ord('A')
        p = (c - key[i]) % 26
        decrypted += chr(p + ord('A'))
    else:
        decrypted += ciphertext[i]

print("Decrypted Text:")
print(decrypted)