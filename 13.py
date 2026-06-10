key = [[9, 4],
       [5, 7]]

plain = input("Enter Plain Text (2 letters): ").lower()

a = ord(plain[0]) - 97
b = ord(plain[1]) - 97

c1 = (key[0][0] * a + key[0][1] * b) % 26
c2 = (key[1][0] * a + key[1][1] * b) % 26

cipher = chr(c1 + 65) + chr(c2 + 65)

print("Cipher Text:", cipher)