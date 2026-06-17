from Crypto.Cipher import AES
from Crypto.Util.Padding import pad

key = b'1234567890ABCDEF'

cipher = AES.new(key, AES.MODE_ECB)

X = b'HELLO1234567890'

# One-block MAC
T = cipher.encrypt(X)

print("Original MAC:", T.hex())

# Forge second block
X2 = bytes([a ^ b for a, b in zip(X, T)])

# Verify
C1 = cipher.encrypt(X)
C2 = cipher.encrypt(bytes([a ^ b for a, b in zip(X2, C1)]))

print("Forged MAC:", C2.hex())

if T == C2:
    print("Forgery Successful")
else:
    print("Forgery Failed")