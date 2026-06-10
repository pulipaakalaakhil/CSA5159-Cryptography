
cipher = input("Enter Cipher Text: ")

freq = {}

for ch in cipher:
    if ch != ' ':
        freq[ch] = freq.get(ch, 0) + 1

print("\nFrequency of Symbols:")
for ch, count in sorted(freq.items(), key=lambda x: x[1], reverse=True):
    print(ch, ":", count)