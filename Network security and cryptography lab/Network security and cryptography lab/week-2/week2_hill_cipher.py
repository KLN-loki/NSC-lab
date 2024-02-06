import numpy as np

def generate_key_matrix(key):
    key = key.replace(" ", "").upper()
    key_len = len(key)
    matrix_size = int(key_len ** 0.5)
    key_matrix = [ord(char) - 65 for char in key]

    while len(key_matrix) % matrix_size != 0:
        key_matrix.append(0)

    return np.array(key_matrix).reshape(matrix_size, matrix_size)

def hill_encrypt(message, key):
    key_matrix = generate_key_matrix(key)
    matrix_size = key_matrix.shape[0]

    message = message.replace(" ", "").upper()

    while len(message) % matrix_size != 0:
        message += 'X'

    message_matrix = [ord(char) - 65 for char in message]
    message_matrix = np.array(message_matrix).reshape(-1, matrix_size)

    encrypted_text = ""
    for row in message_matrix:
        row = np.dot(row, key_matrix) % 26
        encrypted_text += ''.join([chr(char + 65) for char in row])

    return encrypted_text


def mod_mat_inv(matrix, modulus):
    det = int(np.round(np.linalg.det(matrix)))
    det_inv = pow(det, -1, modulus)
    adjugate = np.round(det * np.linalg.inv(matrix)).astype(int) % modulus
    inverse = (det_inv * adjugate) % modulus
    return inverse


def hill_decrypt(ciphertext, key):
    key_matrix = generate_key_matrix(key)
    key_inverse = mod_mat_inv(key_matrix, 26)
    matrix_size = key_matrix.shape[0]

    ciphertext = ciphertext.replace(" ", "").upper()

    ciphertext_matrix = [ord(char) - 65 for char in ciphertext]
    ciphertext_matrix = np.array(ciphertext_matrix).reshape(-1, matrix_size)

    decrypted_text = ""
    for row in ciphertext_matrix:
        row = np.dot(row, key_inverse) % 26
        decrypted_text += ''.join([chr(char + 65) for char in row])

    decrypted_text = decrypted_text.rstrip('X')

    return decrypted_text
message = input("Enter the Plain text : ")
key = input("Enter the Key string : ")

encrypted_message = hill_encrypt(message, key)
print("Encrypted:", encrypted_message)

decrypted_message = hill_decrypt(encrypted_message, key)

print("Decrypted:", decrypted_message)
