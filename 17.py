shift_schedule = [1, 1, 2, 2, 2, 2, 2, 2,
                  1, 2, 2, 2, 2, 2, 2, 1]

print("Encryption Keys:")
for i in range(16):
    print("K" + str(i+1), "Shift =", shift_schedule[i])

print("\nDecryption Key Order:")
for i in range(16, 0, -1):
    print("K" + str(i), end=" ")