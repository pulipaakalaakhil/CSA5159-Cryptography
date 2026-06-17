def encrypt(m, e, n):
    return pow(m, e, n)

# Example RSA values
p = 61
q = 53
n = p * q
e = 17

# Build attack table
lookup = {}

for m in range(26):
    c = encrypt(m, e, n)
    lookup[c] = chr(m + 65)

print("Ciphertext Lookup Table")

for c, ch in lookup.items():
    print(c, "->", ch)

# Example encrypted message
message = "HELLO"

cipher = [encrypt(ord(ch)-65, e, n) for ch in message]

print("\nCiphertext:")
print(cipher)

# Attack
decrypted = ""

for c in cipher:
    decrypted += lookup[c]

print("\nRecovered Message:")
print(decrypted)