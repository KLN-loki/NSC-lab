def diffie_hellman(p, g, a, b):
  A = pow(g, a, p)
  B = pow(g, b, p)
  s = pow(B, a, p)
  return s

p = 17
g = 5
a = 4
b = 6

shared_key = diffie_hellman(p, g, a, b)
print(f"Shared secret key: {shared_key}")
