BLOCK_SIZE = 8

def pad(data):
    data += b'\x80'

    while len(data) % BLOCK_SIZE != 0:
        data += b'\x00'

    return data

msg = b"HELLO123"

padded = pad(msg)

print("Original Length:", len(msg))
print("Padded Length:", len(padded))
print("Padded Data:", padded)