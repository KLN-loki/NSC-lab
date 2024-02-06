'''import math
def gcd(a,b):
    t=0
    while(1):
        t=a%b
        if t==0:
            return b
        a=b
        b=t

text=int(input("Enter the data:"))
p=61
q=53
n=p*q
f=(p-1)*(q-1)
e=2
while(e<f):
    if gcd(f,e)==1:
        break
    e+=1
k=1
d=0
while((d*e)%f!=1):
    d+=1
print(p,q,n,f,e)

print(d)
en=math.fmod(text**e,n)
print("The encrypted text is:",en)
de=math.fmod(en**d,n)
print("original mesagge:",de)'''