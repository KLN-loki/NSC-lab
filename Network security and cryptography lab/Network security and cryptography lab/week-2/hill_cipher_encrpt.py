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

message = input("please give the Plain text : ")
key = input("give the Key : ")

encrypted_message = hill_encrypt(message, key)
print("Encrypted:", encrypted_message)
