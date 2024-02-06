def caesar_cipher(text, shift):
    etext = ""

    for char in text:
        if char.isalnum(): 
            if char.isalpha():
                if char.isupper():
                    echar = chr(((ord(char) - ord('A') + shift) % 26) + ord('A'))
                else:
                    echar = chr(((ord(char) - ord('a') + shift) % 26) + ord('a'))
            else: 
                new_num = (int(char) + shift) % 10  
                echar = str(new_num)
        else:
            echar = chr((ord(char) + shift) % 256)  
        etext += echar

    return etext

while True:
    choice = input("Enter 'E' to encrypt or 'D' to decrypt a message: ").upper()

    if choice == 'E':
        plaintext = input("Enter your text to encrypt: ")
        shift = int(input("Enter the key: "))

        etext = caesar_cipher(plaintext, shift)
        print("Encrypted:", etext)

    elif choice == 'D':
        plaintexttext = input("Enter the text to decrypt: ")
        shift = int(input("Enter the key: "))

        dtext = caesar_cipher(plaintexttext, -shift)
        print("Decrypted:", dtext)

    else:
        print("Please enter a correct choice.")
