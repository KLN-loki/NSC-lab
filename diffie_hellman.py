def mod_exp(base, exponent, modulus):
    result = 1
    base = base % modulus
    while exponent > 0:
        if exponent % 2 == 1:
            result = (result * base) % modulus
        exponent = exponent // 2
        base = (base * base) % modulus
    return result


def diffie_hellman():

    p = int(input("Enter p: "))
    g = int(input("Enter primitive root : "))

    a = int(input("Enter A's secret key: "))

    b = int(input("Enter B's secret key: "))

    A = mod_exp(g, a, p)

    B = mod_exp(g, b, p)

    print("A Sent to B : ", A)
    print("B Sent to A : ", B)

    secret_key_alice = mod_exp(B, a, p)

    secret_key_bob = mod_exp(A, b, p)

    print("Shared secret key for A:", secret_key_alice)
    print("Shared secret key for B:", secret_key_bob)


if __name__ == "__main__":
    diffie_hellman()