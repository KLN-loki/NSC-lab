import random

def is_prime(n, k=5):
    """
    Miller-Rabin primality test.

    Parameters:
    - n: The number to be tested for primality.
    - k: The number of rounds of testing. Higher values of k increase the accuracy.

    Returns:
    - True if n is likely to be prime, False otherwise.
    """
    if n <= 1:
        return False
    if n == 2 or n == 3:
        return True
    if n % 2 == 0:
        return False

    # Write n as 2^r * d + 1
    r, d = 0, n - 1
    while d % 2 == 0:
        r += 1
        d //= 2

    # Witness loop
    for _ in range(k):
        a = random.randint(2, n - 2)
        x = pow(a, d, n)

        if x == 1 or x == n - 1:
            continue

        for _ in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False  # Not prime

    return True  # Likely prime

# Example usage
number_to_test = 1031
rounds_of_testing = 5

if is_prime(number_to_test, rounds_of_testing):
    print(f"{number_to_test} is likely to be a prime number.")
else:
    print(f"{number_to_test} is not a prime number.")
