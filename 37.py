from collections import Counter

cipher = input("Ciphertext: ").upper()

freq = Counter(cipher)

for letter, count in freq.most_common():
    if letter.isalpha():
        print(letter, ":", count)