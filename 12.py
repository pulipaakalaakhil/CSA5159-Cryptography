key = [[9, 4],
       [5, 7]]

inverse_key = [[5, 12],
               [15, 25]]

text = input("Enter Plain Text: ").replace(" ", "").lower()

if len(text) % 2 != 0:
    text += 'x'

cipher = ""

# Encryption
for i in range(0, len(text), 2):
    a = ord(text[i]) - 97
    b = ord(text[i + 1]) - 97

    c1 = (key[0][0] * a + key[0][1] * b) % 26
    c2 = (key[1][0] * a + key[1][1] * b) % 26

    cipher += chr(c1 + 65)
    cipher += chr(c2 + 65)

print("Cipher Text:", cipher)

# Decryption
plain = ""

cipher = cipher.lower()

for i in range(0, len(cipher), 2):
    a = ord(cipher[i]) - 97
    b = ord(cipher[i + 1]) - 97

    p1 = (inverse_key[0][0] * a + inverse_key[0][1] * b) % 26
    p2 = (inverse_key[1][0] * a + inverse_key[1][1] * b) % 26

    plain += chr(p1 + 97)
    plain += chr(p2 + 97)

print("Decrypted Text:", plain)