def generate_keypair(p, q):
   n = p * q
   phi = (p - 1) * (q - 1)
   e = 65537
   d = pow(e, -1, phi)
   return ((e, n), (d, n))

def encrypt(public_key, plaintext):
    e, n = public_key
    cipher = [chr(pow(ord(char), e, n)) for char in plaintext]
    return ''.join(cipher)

def decrypt(private_key, ciphertext):
    d, n = private_key
    plain = [chr(pow(ord(char), d, n)) for char in ciphertext]
    return ''.join(plain)


p = 101
q = 131
plaintext = "Indra eerababu"

public_key, private_key = generate_keypair(p, q)
encrypted_msg = encrypt(public_key, plaintext)
decrypted_msg = decrypt(private_key, encrypted_msg)

print("Encrypted message:", encrypted_msg)
print("Decrypted message:", decrypted_msg)
