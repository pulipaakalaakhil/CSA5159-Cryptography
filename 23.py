# Counter (CTR) Mode Encryption and Decryption

plaintext = [1, 2, 4]
key = 15

counter = 0
ciphertext = []

# Encryption
for p in plaintext:
    keystream = counter ^ key
    c = p ^ keystream
    ciphertext.append(c)
    counter += 1

print("Ciphertext:", ciphertext)

# Decryption
counter = 0
decrypted = []

for c in ciphertext:
    keystream = counter ^ key
    p = c ^ keystream
    decrypted.append(p)
    counter += 1

print("Decrypted Plaintext:", decrypted)