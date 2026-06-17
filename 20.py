# ECB Mode Simulation

key = 5

# Plaintext blocks
P1 = 10
P2 = 20
P3 = 30

# Encryption
C1 = P1 + key
C2 = P2 + key
C3 = P3 + key

print("Original Ciphertext:")
print(C1, C2, C3)

# Error introduced in C1
C1 = C1 + 1

# Decryption
D1 = C1 - key
D2 = C2 - key
D3 = C3 - key

print("\nAfter Error in C1:")
print("P1 =", D1)
print("P2 =", D2)
print("P3 =", D3)