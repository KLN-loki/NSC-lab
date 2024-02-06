import numpy as np

# Step 1: Define matrix size and key
matrix_size = int(4**0.5)
key = "DCDF"

# Step 2: Create key matrix by converting characters to ASCII values
key_matrix = [ord(char) - 65 for char in key]
print("Key Matrix (Before Padding):", key_matrix)

# Step 3: Pad key matrix with zeros to make it a square matrix
while len(key_matrix) % matrix_size != 0:
    key_matrix.append(0)
    print("Key Matrix (After Padding):", key_matrix)

# Step 4: Reshape the key matrix to a square matrix
key_matrix = np.array(key_matrix).reshape(matrix_size, matrix_size)
print("Key Matrix (After Reshaping):")
print(key_matrix)

# Step 5: Encrypting a message
message = 'TEXT'
message_matrix = [ord(char) - 65 for char in message]
print("Message Matrix (Before Reshaping):", message_matrix)

# Reshape the message matrix to a square matrix
message_matrix = np.array(message_matrix).reshape(matrix_size, matrix_size)
print("Message Matrix (After Reshaping):")
print(message_matrix)

# Encrypt the message using the key matrix
encrypted_text = ""
for row in message_matrix:
    row = np.dot(row, key_matrix) % 26
    print("Encrypted Row:", row)
    encrypted_text += ''.join([chr(char + 65) for char in row])
print("The encrypted text is:", encrypted_text)

# Step 6: Calculating the inverse of the key matrix for decryption
print("\n\nCalculating the inverse:\n\n")

matrix_inv = np.linalg.inv(key_matrix)
print("The key matrix inverse is:\n", matrix_inv)

det = int(np.round(np.linalg.det(key_matrix)))
print("\nThe determinant of the key matrix is:\n", det)

det_inv = pow(det, -1, 26)
print("\nThe inverse after performing some operations is:\n", det_inv)

inverse_matrix = (det_inv * matrix_inv) % 26
print("\nThe final inverse for decryption is:\n", inverse_matrix)

# Step 7: Decrypting the message
print("\n\nCalculating the decryption:\n\n")

key_inverse = np.linalg.inv(key_matrix) % 26  # Directly calculate the inverse and apply modulus
ciphertext_matrix = [ord(char) - 65 for char in encrypted_text]
ciphertext_matrix = np.array(ciphertext_matrix).reshape(-1, matrix_size)

decrypted_text = ""
for row in ciphertext_matrix:
    row = np.dot(row, key_inverse) % 26
    decrypted_text += ''.join([chr(int(char) + 65) for char in row])
print("\n\nThe text after decryption is:", decrypted_text)
