# RSA Private Key Calculation

e = 31
n = 3599

# Find p and q
for i in range(2, int(n**0.5) + 1):
    if n % i == 0:
        p = i
        q = n // i
        break

phi = (p - 1) * (q - 1)

# Extended Euclidean Algorithm
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

print("p =", p)
print("q =", q)
print("phi(n) =", phi)
print("Private Key (d, n) = ({}, {})".format(d, n))