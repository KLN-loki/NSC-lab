import math

def encrypt_message(message, key):
    col = len(key)
    row = int(math.ceil(len(message) / col))
    fill_null = row * col - len(message)
    message += '_' * fill_null
    matrix = [message[i:i+col] for i in range(0, len(message), col)]
    cipher = ''.join(matrix[i][key.index(k)] for k in sorted(key) for i in range(row))
    return cipher

def decrypt_message(cipher, key):
    col = len(key)
    row = int(math.ceil(len(cipher) / col))
    key_sorted = sorted(key)
    matrix = [[''] * col for _ in range(row)]
    index = 0
    for k in key_sorted:
        col_index = key.index(k)
        for j in range(row):
            matrix[j][col_index] = cipher[index]
            index += 1
    decrypted_message = ''.join(''.join(row) for row in matrix).rstrip('_')
    return decrypted_message

# Driver Code
msg = "Geeks for Geeks"
key = "HACK"

cipher = encrypt_message(msg, key)
print("Encrypted Message:", cipher)

decrypted_msg = decrypt_message(cipher, key)
print("Decrypted Message:", decrypted_msg)
