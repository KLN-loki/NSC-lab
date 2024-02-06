import sympy
def key():
    p=sympy.randprime(2,1000)
    q=sympy.randprime(2,1000)
    n=p*q
    f=(p-1)*(q-1)
    e=2
    while(sympy.gcd(e,f)!=1):
        e+=1
    d=sympy.mod_inverse(e,f)
    p_key=(e,n)
    pr_key=(d,n)
    return p_key,pr_key

def encrypt(public_key, plaintext):
    e, n = public_key
    cipher = [pow(ord(char), e, n) for char in plaintext]
    for i in cipher:
        print(chr((i%97)+97),end=" ")kl
    print()
    return cipher

def decrypt(private_key, ciphertext):
    d, n = private_key
    plain = [chr(pow(char, d, n)) for char in ciphertext]
    return ''.join(plain)

text=input("Enter the Text:")
p,pr=key()
l=[]
print(text)
print("public key:",p)
print("private key:",pr)
en_text = encrypt(p, text)

#print("Encrypted:",' '.join(map(str, en_text)))
dec_text = decrypt(pr, en_text)
print("original text:",dec_text)