def generate_matrix(key):
    key = key.upper().replace("J", "I")
    matrix = []
    used = set()

    for ch in key:
        if ch.isalpha() and ch not in used:
            matrix.append(ch)
            used.add(ch)

    for ch in "ABCDEFGHIKLMNOPQRSTUVWXYZ":
        if ch not in used:
            matrix.append(ch)

    return [matrix[i:i+5] for i in range(0, 25, 5)]

def find_pos(matrix, ch):
    if ch == 'J':
        ch = 'I'
    for i in range(5):
        for j in range(5):
            if matrix[i][j] == ch:
                return i, j

def decrypt_pair(matrix, a, b):
    r1, c1 = find_pos(matrix, a)
    r2, c2 = find_pos(matrix, b)

    if r1 == r2:  # same row
        return matrix[r1][(c1-1)%5] + matrix[r2][(c2-1)%5]

    elif c1 == c2:  # same column
        return matrix[(r1-1)%5][c1] + matrix[(r2-1)%5][c2]

    else:  # rectangle rule
        return matrix[r1][c2] + matrix[r2][c1]

key = "ROYALNEWZEALANDNAVY"

cipher = """KXJEYUREBEZWEHEWRYTUHEYFS
KREHEGOYFIWTTTUOLKSYCAJPO
BOTEIZONTXBYBNTGONEYCUZWR
GDSONSXBOUYWRHEBAAHYUSEDQ"""

cipher = cipher.replace(" ", "").replace("\n", "")

matrix = generate_matrix(key)

print("Playfair Matrix:")
for row in matrix:
    print(row)

plaintext = ""

for i in range(0, len(cipher), 2):
    plaintext += decrypt_pair(matrix, cipher[i], cipher[i+1])

print("\nDecrypted Text:")
print(plaintext)