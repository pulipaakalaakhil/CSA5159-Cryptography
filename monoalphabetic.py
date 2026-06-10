alphabet = "abcdefghijklmnopqrstuvwxyz"
keyword = "CIPHER"

# Generate cipher sequence
cipher = keyword
for ch in alphabet.upper():
    if ch not in cipher:
        cipher += ch

print("Plain :", alphabet)
print("Cipher:", cipher)

# Encryption
text = input("Enter plaintext: ").lower()
encrypted = ""

for ch in text:
    if ch.isalpha():
        encrypted += cipher[alphabet.index(ch)]
    else:
        encrypted += ch

print("Encrypted Text:", encrypted)