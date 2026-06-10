# Affine Cipher

a = 5
b = 8

text = input("Enter Plain Text: ").upper()

# Encryption
cipher = ""

for ch in text:
    if ch.isalpha():
        x = ord(ch) - ord('A')
        y = (a * x + b) % 26
        cipher += chr(y + ord('A'))
    else:
        cipher += ch

print("Encrypted Text:", cipher)

# Decryption
a_inv = 21   # Modular inverse of 5

plain = ""

for ch in cipher:
    if ch.isalpha():
        y = ord(ch) - ord('A')
        x = (a_inv * (y - b)) % 26
        plain += chr(x + ord('A'))
    else:
        plain += ch

print("Decrypted Text:", plain)