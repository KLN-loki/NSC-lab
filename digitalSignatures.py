import hashlib
import random
from math import gcd

p = 23
g = 5

def generate_private_key(p):
    return random.randint(1, p - 1)

def generate_public_key(p, g, x):
    return pow(g, x, p)

def sign_message(message, p, g, x):
    while True:
        k = random.randint(1, p - 1)
        r = pow(g, k, p) % p
        h = int(hashlib.sha256(message.encode()).hexdigest(), 16)
        s = (x * r + k * h) % (p - 1)
        if gcd(s, p - 1) == 1:
            break
    return r, s

def verify_signature(message, r, s, p, g, y):
    h = int(hashlib.sha256(message.encode()).hexdigest(), 16)
    w = pow(s, -1, p - 1)
    u1 = (h * w) % (p - 1)
    u2 = (r * w) % (p - 1)
    v = (pow(g, u1, p) * pow(y, u2, p)) % p
    return v == r

message = input("Enter the message to sign: ")
x = generate_private_key(p)
y = generate_public_key(p, g, x)
r, s = sign_message(message, p, g, x)
print(f"Message: {message}")
print(f"Public Key (y): {y}")
print(f"Signature (r, s): ({r}, {s})")
print(f"Signature verified: {verify_signature(message, r, s, p, g, y)}")

# import hashlib
# import sys

# def hash(a):
#     result = hashlib.sha1(a.encode())
#     a = result.hexdigest()
#     res = int(a, 16)
#     return res

# # p = int(input("Enter p value : "))
# p = 11
# # q = int(input("Enter q value as prime divisor of p-1 : "))
# q = 5
# # h = int(input("Enter h value in range of 1 t0 p-1 : "))
# h = 10
# g = pow(h, (p-1)//q, p)

# print("The value of g is : ", g)

# # x = int(input("Enter user private key :"))
# x = 5
# y = pow(g, x, p)

# # k = int(input("Enter k value in range of o to q : "))
# k = 3
# r = pow(pow(g, k, p), 1, q)

# x1 = 1
# while (k * x1) % q != 1:
#     x1 += 1

# # h = input("Enter message :")
# h = 'hello'  
# h1 = hash(h)

# print("The h1 value is ", h1 )

# s = pow(x1 * (h1 + x * r), 1, q)

# print("The value of r and s is : ", r ,s)

# if s == 0 or r == 0:
#     print("invalid")
#     sys.exit(0)

# s1 = 1
# while (s1 * s) % q != 1:
#     s1 += 1

# w = pow(s1, 1, q)

# # ha = input("Enter msg after transmission :")
# ha = 'hello'
# h2 = hash(ha)

# print("the value of h2 ", h2)

# u1 = (h2 * w) % q
# u2 = (r * w) % q

# v = ((pow(g, u1) * pow(y, u2)) % q) % p

# print(u1, u2, y, v, r)

# if v == r:
#     print("valid")
# else:
#     print("Not valid")