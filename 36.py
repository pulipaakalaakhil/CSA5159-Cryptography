def affine_encrypt(text, a, b):
    result = ""
    for ch in text.upper():
        if ch.isalpha():
            p = ord(ch) - 65
            c = (a * p + b) % 26
            result += chr(c + 65)
    return result

text = input("Text: ")
a = int(input("a: "))
b = int(input("b: "))

print("Cipher:", affine_encrypt(text, a, b))