from collections import Counter

cipher = input("Ciphertext: ").upper()

freq = Counter(cipher)

print("Top 10 Frequent Letters:")

for letter, count in freq.most_common(10):
    print(letter, ":", count)