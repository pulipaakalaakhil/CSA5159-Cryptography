# Caesar Cipher

text = input("Enter Plain Text: ").upper()
shift = 3

cipher = ""

for ch in text:
    if ch.isalpha():

        # Step 1: Convert letter to number
        p = ord(ch) - ord('A')

        # Step 2: Add shift and apply modulo 26
        c = (p + shift) % 26

        # Step 3: Convert number back to letter
        cipher += chr(c + ord('A'))

    else:
        cipher += ch

print("Encrypted Text:", cipher)