def ceaser_cipher(text,Shift):
    temp = ''
    for char in text:
        enc = (ord(char)+Shift)%256
        temp+=chr(enc)
    return temp

Shift = int(input('Enter the shift value : '))
pt = input('Enter the string to perform the encryption : ')
b = ceaser_cipher(pt,Shift).upper()
print("After encryption the cipher text is : ",b)
decrypt = ceaser_cipher(b,-Shift)
print("After decryption the string is : ", decrypt)
        
    