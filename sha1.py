import struct

def left_rotate(n, b):
    return ((n << b) | (n >> (32 - b))) & 0xffffffff

def sha1(message):
    h0 = 0x67452301
    h1 = 0xEFCDAB89
    h2 = 0x98BADCFE
    h3 = 0x10325476
    h4 = 0xC3D2E1F0
    original_byte_len = len(message)
    original_bit_len = original_byte_len * 8
    message += b'\x80'
    message += b'\x00' * ((56 - (original_byte_len + 1) % 64) % 64)
    message += struct.pack('>Q', original_bit_len)
    for i in range(0, len(message), 64):
        chunk = message[i:i + 64]
        w = [0] * 80
        for j in range(16):
            w[j] = struct.unpack('>I', chunk[j * 4:j * 4 + 4])[0]
        for j in range(16, 80):
            w[j] = left_rotate(w[j - 3] ^ w[j - 8] ^ w[j - 14] ^ w[j - 16], 1)
        a = h0
        b = h1
        c = h2
        d = h3
        e = h4
        for j in range(80):
            if j <= 19:
                f = (b & c) | ((~b) & d)
                k = 0x5A827999
            elif j <= 39:
                f = b ^ c ^ d
                k = 0x6ED9EBA1
            elif j <= 59:
                f = (b & c) | (b & d) | (c & d)
                k = 0x8F1BBCDC
            else:
                f = b ^ c ^ d
                k = 0xCA62C1D6
            temp = left_rotate(a, 5) + f + e + k + w[j] & 0xffffffff
            e = d
            d = c
            c = left_rotate(b, 30)
            b = a
            a = temp
        h0 = (h0 + a) & 0xffffffff
        h1 = (h1 + b) & 0xffffffff
        h2 = (h2 + c) & 0xffffffff
        h3 = (h3 + d) & 0xffffffff
        h4 = (h4 + e) & 0xffffffff
    return '%08x%08x%08x%08x%08x' % (h0, h1, h2, h3, h4)

message = input("Enter a message: ").encode()
print('SHA-1:', sha1(message))

# import struct

# def left_rotate(n, b):
#     return ((n << b) | (n >> (32 - b))) & 0xffffffff

# def padding(message):
#     original_byte_len = len(message)
#     original_bit_len = original_byte_len * 8

#     # Append a single '1' bit and then '0' bits
#     message += b'\x80'
#     while len(message) % 64 != 56:
#         message += b'\x00'

#     # Append original length of message (before padding)
#     message += struct.pack('>Q', original_bit_len)

#     return message

# def process_block(block, h0, h1, h2, h3, h4):
#     w = [0]*80
#     for i in range(16):
#         w[i] = struct.unpack('>I', block[i*4:i*4 + 4])[0]
#     for i in range(16, 80):
#         w[i] = left_rotate(w[i-3] ^ w[i-8] ^ w[i-14] ^ w[i-16], 1)

#     a, b, c, d, e = h0, h1, h2, h3, h4

#     for i in range(80):
#         if 0 <= i <= 19:
#             f = d ^ (b & (c ^ d))
#             k = 0x5A827999
#         elif 20 <= i <= 39:
#             f = b ^ c ^ d
#             k = 0x6ED9EBA1
#         elif 40 <= i <= 59:
#             f = (b & c) | (d & (b | c))
#             k = 0x8F1BBCDC
#         elif 60 <= i <= 79:
#             f = b ^ c ^ d
#             k = 0xCA62C1D6

#         temp = left_rotate(a, 5) + f + e + k + w[i] & 0xffffffff
#         e = d
#         d = c
#         c = left_rotate(b, 30)
#         b = a
#         a = temp

#     h0 = (h0 + a) & 0xffffffff
#     h1 = (h1 + b) & 0xffffffff
#     h2 = (h2 + c) & 0xffffffff
#     h3 = (h3 + d) & 0xffffffff
#     h4 = (h4 + e) & 0xffffffff

#     return h0, h1, h2, h3, h4

# def sha1(message):
#     message = padding(message)

#     h0 = 0x67452301
#     h1 = 0xEFCDAB89
#     h2 = 0x98BADCFE
#     h3 = 0x10325476
#     h4 = 0xC3D2E1F0

#     for i in range(0, len(message), 64):
#         h0, h1, h2, h3, h4 = process_block(message[i:i+64], h0, h1, h2, h3, h4)

#     return '{:08x}{:08x}{:08x}{:08x}{:08x}'.format(h0, h1, h2, h3, h4)

# # Test the function
# msg = b"kln"
# print(f"SHA-1 Hash of '{msg}' is: {sha1(msg)}")
