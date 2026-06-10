text=input("Enter the plain text:").upper()
plain="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
cipher="QWERTYUIOPLKJHGFDSAXZCVBNM"

encrypted=""
for ch in text:
    if ch in plain:
        encrypted+=cipher[plain.index(ch)]
    else:
        encrypted+=ch

print("Encrypted cipher text:",encrypted)

decrypted=""
for ch in encrypted:
    if ch in cipher:
        decrypted+=plain[cipher.index(ch)]
    else:
        decrypted+=ch

print("Decrypted plain text:",decrypted)
