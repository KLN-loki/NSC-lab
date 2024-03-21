import numpy as np
from math import sqrt
from sympy import Matrix


plainText = input("Enter the plain text: ")
key = input("Enter the key: ")

key_length = len(key)
text_length = len(plainText)
key_matrix_dim = int(sqrt(key_length))


def construct_matrix(text, key):
    key_matrix = np.array([ord(i)-ord('A') for i in key])
    key_matrix = key_matrix.reshape(key_matrix_dim, key_matrix_dim)

    text_matrix = np.array([ord(i)-ord('A') for i in text])
    text_matrix = text_matrix.reshape(
        text_length//key_matrix_dim, key_matrix_dim)

    return key_matrix, text_matrix


def Encryption():
    key_matrix, plainText_matrix = construct_matrix(plainText, key)
    cipher = np.array([])
    for i in range(text_length // key_matrix_dim):
        row = np.matmul(key_matrix, plainText_matrix[i])
        cipher = np.append(cipher, list(map(chr, row % 26 + ord('A'))))
    return cipher


cipher_matrix = Encryption()
print("Cipher text: ", "".join(cipher_matrix.flatten()))


def Decryption():
    key_matrix, Cipher_matrix = construct_matrix(cipher_matrix, key)
    A = Matrix(key_matrix)
    key_matrix_inv = A.inv_mod(26)
    text = np.array([])
    for i in range(text_length // key_matrix_dim):
        row = np.matmul(key_matrix_inv, Cipher_matrix[i])
        text = np.append(text, list(map(chr, row % 26 + ord('A'))))
    return text


print("Plaintext: ", "".join(Decryption()))