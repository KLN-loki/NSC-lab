import numpy as np

# Step 1: Define matrix size and key
matrix_size = int(4**0.5)
key = "DCDF"

# Step 2: Create key matrix by converting characters to ASCII values
key_matrix = np.array([ord(char) - 65 for char in key]).reshape(matrix_size, matrix_size)
print("Key Matrix:", key_matrix)

# Step 3: Check if the key matrix is invertible
if np.linalg.det(key_matrix) == 0:
    print("Error: The key matrix is not invertible and cannot be used for Hill Cipher encryption/decryption.")
else:
    # Step 4: Encrypting a message
    message = 'TEXT'
    message_matrix = np.array([ord(char) - 65 for char in message]).reshape(matrix_size, matrix_size)
    print("Message Matrix:", message_matrix)

    # Encrypt the message using the key matrix
    encrypted_text = ""
    for row in message_matrix:
        row = np.dot(row, key_matrix) % 26
        encrypted_text += ''.join([chr(char + 65) for char in row])
    print("The encrypted text is:", encrypted_text)

    # Step 5: Decrypting the message
    key_inverse = np.linalg.inv(key_matrix) % 26
    ciphertext_matrix = np.array([ord(char) - 65 for char in encrypted_text]).reshape(-1, matrix_size)

    decrypted_text = ""
    for row in ciphertext_matrix:
        # Ensure proper integer conversion before adding 65 to avoid character overflow
        row = np.dot(row, key_inverse) % 26
        decrypted_text += ''.join([chr(int(char) + 65) for char in row])  # Corrected line
    print("The text after decryption is:", decrypted_text)
