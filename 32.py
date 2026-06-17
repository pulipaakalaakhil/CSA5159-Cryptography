import random

message = 100

# DSA-like simulation
for i in range(2):
    k = random.randint(1, 1000)
    r = k % 97
    s = (message + k) % 97

    print("DSA Signature", i+1, ":", (r, s))

# RSA-like simulation
rsa_signature = pow(message, 7, 143)

print("\nRSA Signature 1:", rsa_signature)
print("RSA Signature 2:", rsa_signature)