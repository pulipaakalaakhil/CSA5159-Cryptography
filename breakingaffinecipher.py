a = 3
b = 15

# Find inverse of a modulo 26
for i in range(26):
    if (a * i) % 26 == 1:
        a_inv = i
        break

cipher = input("Enter Cipher Text: ").upper()

plain = ""

for ch in cipher:
    if ch.isalpha():
        c = ord(ch) - 65
        p = (a_inv * (c - b)) % 26
        plain += chr(p + 65)
    else:
        plain += ch

print("Decrypted Text:", plain)