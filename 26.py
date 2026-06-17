from math import gcd

# Extended Euclidean Algorithm
def mod_inverse(a, m):
    m0 = m
    x0, x1 = 0, 1

    while a > 1:
        q = a // m
        a, m = m, a % m
        x0, x1 = x1 - q * x0, x0

    return x1 + m0 if x1 < 0 else x1

# Example RSA values
p = 61
q = 53
n = p * q
phi = (p - 1) * (q - 1)

e = 17
d = mod_inverse(e, phi)

print("Public Key (e,n):", (e, n))
print("Private Key d:", d)

# Bob generates new e and d but keeps same n
new_e = 7
new_d = mod_inverse(new_e, phi)

print("\nNew Public Key:", (new_e, n))
print("New Private Key:", new_d)

print("\nUnsafe: Same modulus n is reused.")