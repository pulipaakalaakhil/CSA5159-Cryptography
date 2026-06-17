# CBC Mode Encryption and Decryption

plaintext = [1, 2, 3]
key = 15
iv = 170   # 10101010 in decimal

# Encryption
ciphertext = []
prev = iv

for p in plaintext:
    c = (p ^ prev) ^ key
    ciphertext.append(c)
    prev = c

print("Ciphertext:", ciphertext)

# Decryption
decrypted = []
prev = iv

for c in ciphertext:
    p = (c ^ key) ^ prev
    decrypted.append(p)
    prev = c

print("Decrypted Plaintext:", decrypted)