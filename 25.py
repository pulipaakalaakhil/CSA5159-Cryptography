import math

# Public Key
n = int(input("Enter n: "))
e = int(input("Enter e: "))

# Plaintext block known to share a factor with n
M = int(input("Enter plaintext block M: "))

# Find common factor
p = math.gcd(M, n)

if p == 1:
    print("No common factor found.")
else:
    q = n // p

    phi = (p - 1) * (q - 1)

    # Modular inverse using Extended Euclidean Algorithm
    def mod_inverse(a, m):
        m0 = m
        x0, x1 = 0, 1

        while a > 1:
            q = a // m
            a, m = m, a % m
            x0, x1 = x1 - q * x0, x0

        if x1 < 0:
            x1 += m0

        return x1

    d = mod_inverse(e, phi)

    print("\nFactorization Found!")
    print("p =", p)
    print("q =", q)
    print("phi(n) =", phi)
    print("Private Key d =", d)