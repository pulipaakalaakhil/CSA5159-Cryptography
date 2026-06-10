import math

# Total possible Playfair keys
total_keys = math.factorial(25)

# Effectively unique keys
unique_keys = total_keys // 25

print("Total possible keys =", total_keys)
print("Effectively unique keys =", unique_keys)