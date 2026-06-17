# CBC Mode Encryption (Simple)

plaintext = "HELLO"
key = 5
iv = 10

cipher = []

for ch in plaintext:
    block = ord(ch) ^ iv      # CBC step
    c = block + key           # Encryption
    cipher.append(c)
    iv = c                    # Update IV

print("Ciphertext:", cipher)