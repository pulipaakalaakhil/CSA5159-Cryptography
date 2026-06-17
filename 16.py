from collections import Counter

# English letter frequency order
english_freq = "ETAOINSHRDLCUMWFGYPBVKJXQZ"

cipher = input("Enter ciphertext: ").upper()

# Count letter frequencies
freq = Counter(c for c in cipher if c.isalpha())

# Sort letters by frequency
cipher_freq = ''.join([x[0] for x in freq.most_common()])

# Create substitution mapping
mapping = {}
for i in range(len(cipher_freq)):
    mapping[cipher_freq[i]] = english_freq[i]

# Decrypt
plaintext = ""
for ch in cipher:
    if ch in mapping:
        plaintext += mapping[ch]
    else:
        plaintext += ch

print("\nPossible Plaintext:")
print(plaintext)