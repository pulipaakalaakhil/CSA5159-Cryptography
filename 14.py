plaintext = "sendmoremoney"
key = [9, 0, 1, 7, 23, 15, 21, 14, 11, 11, 2, 8, 9]

cipher = ""

for i in range(len(plaintext)):
    p = ord(plaintext[i]) - ord('a')
    c = (p + key[i]) % 26
    cipher += chr(c + ord('A'))

print("Cipher Text:", cipher)

# Decryption
plain = ""

for i in range(len(cipher)):
    c = ord(cipher[i]) - ord('A')
    p = (c - key[i]) % 26
    plain += chr(p + ord('a'))

print("Decrypted Text:", plain)