def encrypt(s,n):
    st=""
    for i in s:
        if i.isupper():
            st+=chr((ord(i)+n-65)%26+65)
        elif i.islower():
            st+=chr((ord(i)+n-97)%26+65)
        elif 48<=ord(i)<=57:
            st+=chr((ord(i)+n-48)%10+48)
        else:
            st+=i
    return st

def decrypt(s,n):
    st=""
    for i in s:
        if i.isupper():
            st+=chr((ord(i)-n-65)%26+97)
        elif 48<=ord(i)<=57:
            st+=chr((ord(i)-n-48)%10+48)
        else:
            st+=i
    return st

s=input("Enter the plain text:")
n=int(input("Enter number of shifts:"))
st=encrypt(s,n)
print("The cipher text is:"+st)
dst=decrypt(st,n)
print("The original text is:"+dst)  