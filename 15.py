cipher = input("Enter Cipher Text: ").upper()
n = int(input("Enter number of possible plaintexts: "))

for key in range(n):
    plain = ""

    for ch in cipher:
        if ch.isalpha():
            p = (ord(ch) - ord('A') - key) % 26
            plain += chr(p + ord('A'))
        else:
            plain += ch

    print("Key", key, ":", plain)