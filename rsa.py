def is_prime(n):
    """Check if a number is prime."""
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def get_prime_input():
    """Get a prime number as input from the user."""
    while True:
        try:
            num = int(input("Enter a prime number: "))
            if is_prime(num):
                return num
            else:
                print("Please enter a prime number.")
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

def gcd(a, b):
    """Calculate the greatest common divisor of two numbers."""
    while b:
        a, b = b, a % b
    return a

def mod_inverse(a, m):
    """Calculate the modular inverse of a number."""
    m0, x0, x1 = m, 0, 1
    while a > 1:
        q = a // m
        m, a = a % m, m
        x0, x1 = x1 - q * x0, x0
    return x1 + m0 if x1 < 0 else x1

def generate_keypair(p, q):
    """Generate RSA public and private keys."""
    n = p * q
    phi = (p - 1) * (q - 1)

    e = 2
    while gcd(e, phi) != 1:
        e += 1

    d = mod_inverse(e, phi)

    return ((e, n), (d, n))

def encrypt(message, public_key):
    """Encrypt a message using RSA."""
    e, n = public_key
    cipher_text = ''.join([chr(((ord(char) - 65) ** e) % n + 65) for char in message])
    return cipher_text

def decrypt(cipher_text, private_key):
    """Decrypt a message using RSA."""
    d, n = private_key
    plain_text = ''.join([chr(((ord(char) - 65) ** d) % n + 65) for char in cipher_text])
    return plain_text

def main():
    p = get_prime_input()
    q = get_prime_input()

    public_key, private_key = generate_keypair(p, q)

    print("Public Key (e, n):", public_key)
    print("Private Key (d, n):", private_key)

    message = input("Enter a message to encrypt (only uppercase alphabets): ").upper()

    cipher_text = encrypt(message, public_key)
    print("Encrypted Message:", ''.join(cipher_text))

    decrypted_message = decrypt(cipher_text, private_key)
    print("Decrypted Message:", decrypted_message)

if __name__ == "__main__":
    main()
