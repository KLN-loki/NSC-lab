def encrypt_rail_fence(text, key):
    rail = [['\n' for _ in range(len(text))] for _ in range(key)]
    dir_down, row, col = False, 0, 0

    for char in text:
        if (row == 0) or (row == key - 1):
            dir_down = not dir_down
        rail[row][col] = char
        col += 1
        row += 1 if dir_down else -1

    return ''.join(char for row in rail for char in row if char != '\n')

def decrypt_rail_fence(cipher, key):
    rail = [['\n' for _ in range(len(cipher))] for _ in range(key)]
    dir_down, row, col = None, 0, 0

    for i in range(len(cipher)):
        if row == 0:
            dir_down = True
        if row == key - 1:
            dir_down = False
        rail[row][col] = '*'
        col += 1
        row += 1 if dir_down else -1

    index = 0
    for i in range(key):
        for j in range(len(cipher)):
            if rail[i][j] == '*' and index < len(cipher):
                rail[i][j] = cipher[index]
                index += 1

    result = []
    row, col = 0, 0
    for i in range(len(cipher)):
        if row == 0:
            dir_down = True
        if row == key - 1:
            dir_down = False
        if rail[row][col] != '*':
            result.append(rail[row][col])
            col += 1
        row += 1 if dir_down else -1

    return ''.join(result)

# Example usage with user input
plaintext = input("Enter your plain text: ")
key = int(input("Enter your key: "))

encrypted_text = encrypt_rail_fence(plaintext, key)
print("Encrypted Text:", encrypted_text)

decrypted_text = decrypt_rail_fence(encrypted_text, key)
print("Decrypted Text:", decrypted_text)
