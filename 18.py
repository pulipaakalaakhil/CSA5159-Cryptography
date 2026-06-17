key = "10101010101010101010101010101010101010101010101010101010"

left_half = key[:28]
right_half = key[28:]

print("First 28 bits :", left_half)
print("Second 28 bits:", right_half)

subkey1 = left_half[:24]
subkey2 = right_half[:24]

print("First 24 bits of subkey :", subkey1)
print("Second 24 bits of subkey:", subkey2)