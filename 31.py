def left_shift(block, size):
    return ((block << 1) & ((1 << size) - 1))

def generate_subkeys(L, block_size):
    if block_size == 64:
        Rb = 0x1B
    elif block_size == 128:
        Rb = 0x87
    else:
        raise ValueError("Unsupported block size")

    K1 = left_shift(L, block_size)

    if (L >> (block_size - 1)) & 1:
        K1 ^= Rb

    K2 = left_shift(K1, block_size)

    if (K1 >> (block_size - 1)) & 1:
        K2 ^= Rb

    return K1, K2

L = 0x123456789ABCDEF0

K1, K2 = generate_subkeys(L, 64)

print("K1 =", hex(K1))
print("K2 =", hex(K2))