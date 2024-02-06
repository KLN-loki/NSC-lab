def caesar_cipher(text, shift):
    etext = ""

    for char in text:
        if char.isalpha(): 
            if char.isupper():  
                echar = chr(((ord(char)-ord('A')+shift)%26)+ord('A'))
            else:  
                echar = chr(((ord(char)-ord('a')+shift)%26)+ord('a'))
        else:  
            echar = char

        etext += echar  

    return etext.upper()

while True:
    choice = input("Enter 'E' to encrypt or 'D' to decrypt a message : ").upper()

    if choice == 'E':
        plaintext = input("Enter your text to encrypt: ")
        shift = int(input("Enter the key : "))

        etext = caesar_cipher(plaintext, shift)
        print("Encrypted:", etext)

    elif choice == 'D':
        plaintexttext = input("Enter the text to decrypt: ")
        shift = int(input("Enter the key : "))

        dtext = caesar_cipher(plaintexttext, -shift).lower()
        print("Decrypted:", dtext)

    else:
        print("plese enter correct choice")

