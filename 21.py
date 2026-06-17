# ECB, CBC and CFB Mode Simulation

plaintext = [10, 20, 30]
key = 5
IV = 2

# ECB Mode
ecb = []
for p in plaintext:
    ecb.append(p + key)

print("ECB Ciphertext:", ecb)

# CBC Mode
cbc = []
prev = IV
for p in plaintext:
    c = (p ^ prev) + key
    cbc.append(c)
    prev = c

print("CBC Ciphertext:", cbc)

# CFB Mode
cfb = []
prev = IV
for p in plaintext:
    c = p ^ (prev + key)
    cfb.append(c)
    prev = c

print("CFB Ciphertext:", cfb)