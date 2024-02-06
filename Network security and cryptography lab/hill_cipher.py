def hill_encrypt(plain_text, key_arr, x):
    result = ""
    n = len(plain_text) // x + (len(plain_text) % x )
    l = 0
    for _ in range(n):
        p_arr = [[0] for _ in range(x)]
        for j in range(x):
            if l < len(plain_text):
                p_arr[j][0] = ord(plain_text[l]) - ord('A')
                l += 1
            else:
                p_arr[j][0] = 0
        c_arr = [[0] for _ in range(x)]
        for a in range(x):
            for b in range(1):
                c_arr[a][b] = 0
                for c in range(x):
                    c_arr[a][b] += key_arr[a][c] * p_arr[c][b]
                c_arr[a][b] = c_arr[a][b] % 26
        for j in range(x):
            result += chr(c_arr[j][0] + ord('A'))
    return result

def getCofactor(A, temp, p, q, n):
    i, j = 0, 0
    for row in range(n):
        for col in range(n):
            if row != p and col != q:
                temp[i][j] = A[row][col]
                if j == n - 1:
                    j = 0
                    i += 1
                else:
                    j += 1

def determinant(A, n):
    D = 0
    if n == 1:
        return A[0][0]
    temp = [[0] * n for _ in range(n)]
    sign = 1
    for f in range(n):
        getCofactor(A, temp, 0, f, n)
        D += sign * A[0][f] * determinant(temp, n - 1)
        sign = -sign
    return D

def adjoint(A, adj, n):
    sign = 1
    temp = [[0] * (n - 1) for _ in range(n - 1)]
    for i in range(n):
        for j in range(n):
            getCofactor(A, temp, i, j, n)
            sign = 1 if (i + j) % 2 == 0 else -1
            adj[j][i] = sign * determinant(temp, n - 1)

def find_modular_inverse(a):
    a = a % 26
    for x in range(1, 26):
        if (a * x) % 26 == 1:
            return x
    return -1

def hill_decrypt(cipher_text, key_arr, x):
    det = determinant(key_arr, x)
    det_inverse = find_modular_inverse(det)
    if det_inverse == -1:
        print("Cannot find the modular inverse. Choose a different key.")
        return ""
    adj = [[0] * x for _ in range(x)]
    adjoint(key_arr, adj, x)
    for i in range(x):
        for j in range(x):
            adj[i][j] = (adj[i][j] * det_inverse) % 26
            if adj[i][j] < 0:
                adj[i][j] = (adj[i][j] + 26) % 26
    inverse = adj
    decrypted = hill_encrypt(cipher_text, inverse, x)
    return decrypted

if __name__ == "__main__":
    plain_text = input("Enter the plain Text: ").upper()
    key = input("Enter the key: ").upper()
    x = int(len(key) ** 0.5)
    if len(key) / x != x:
        print("The key cannot be converted into a square matrix")
    else:
        key_arr = [[ord(key[i]) - ord('A') for i in range(x * j, x * (j + 1))] for j in range(x)]
        cipher_text = hill_encrypt(plain_text, key_arr, x)
        print("The encrypted cipherText using Hill cipher method is:")
        print(cipher_text)
        decrypted_text=hill_decrypt(cipher_text,key_arr,x)
        print("The decrypted message is:",decrypted_text)          