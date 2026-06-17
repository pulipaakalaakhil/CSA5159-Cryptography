def xor(a, b):
    result = ""

    for i in range(len(a)):
        result += str(int(a[i]) ^ int(b[i]))

    return result

plaintext = "1010101010101010101010101010101010101010101010101010101010101010"

key = "11110000111100001111000011110000111100001111000011110000"

left = plaintext[:32]
right = plaintext[32:]

round_key = key[:32]

f = xor(right, round_key)

new_right = xor(left, f)

cipher = right + new_right

print("Ciphertext:")
print(cipher)