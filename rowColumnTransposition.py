def encrypt(message, key):
    # Determine number of columns based on length of the key
    num_columns = len(key)
    # Determine number of rows based on length of message and number of columns
    num_rows = -(-len(message) // num_columns)  # Ceiling division

    # Pad message with spaces to ensure it fills up the grid completely
    message += ' ' * (num_rows * num_columns - len(message))

    # Create the grid to store the message
    grid = [['' for _ in range(num_columns)] for _ in range(num_rows)]

    # Fill the grid with the message characters
    index = 0
    for i in range(num_rows):
        for j in range(num_columns):
            grid[i][j] = message[index]
            index += 1

    # Encrypt the message based on the key order
    ciphertext = ''
    for col in key:
        col_index = int(col) - 1
        for row in range(num_rows):
            ciphertext += grid[row][col_index]

    return ciphertext


def decrypt(ciphertext, key):
    # Determine number of columns based on length of the key
    num_columns = len(key)
    # Determine number of rows based on length of ciphertext and number of columns
    num_rows = -(-len(ciphertext) // num_columns)  # Ceiling division

    # Create the grid to store the ciphertext
    grid = [['' for _ in range(num_columns)] for _ in range(num_rows)]

    # Fill the grid with the ciphertext characters based on the key order
    index = 0
    for col in key:
        col_index = int(col) - 1
        for row in range(num_rows):
            grid[row][col_index] = ciphertext[index]
            index += 1

    # Extract the plaintext from the grid
    plaintext = ''
    for i in range(num_rows):
        for j in range(num_columns):
            plaintext += grid[i][j]

    return plaintext.strip()


# Example usage:
message = "HELLO WORLD"
key = "2413"

# Encryption
encrypted_message = encrypt(message, key)
print("Encrypted message:", encrypted_message)

# Decryption
decrypted_message = decrypt(encrypted_message, key)
print("Decrypted message:", decrypted_message)
