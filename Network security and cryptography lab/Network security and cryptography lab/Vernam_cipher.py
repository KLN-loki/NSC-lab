def encrypt(key, pt):
    temp = ""
    for i in range(len(pt)):
        char = pt[i]
        temp += chr((ord(char) - 97 + ord(key[i]) - 97) % 26 + 97)
    return temp

def decrypt(key, enc):
    temp = ""
    for i in range(len(enc)):
        char = enc[i]  # Corrected from pt[i]
        temp += chr((ord(char) - ord(key[i]) + 26) % 26 + 97)
    return temp

if __name__ == "__main__":
    while True:
        pt = input("Enter the plain text: ")
        key = input("Enter the key: ")
        if len(pt)!=len(key):
            print("The length of the key and the plain text has to be same")
          
        else:    
            enc = encrypt(key, pt)
            print("After encryption: ", enc)
            dec = decrypt(key, enc)
            print("After decryption: ", dec)
