def lshift(k,n):
   kc = [0]*5
   kc = k.copy()
   l = len(k)
   for i in range(0,l):
     k[i] = kc[(i+n)%l]
   return k

def permute(p,n,b):
      a=[0]*n
      for i in range(0,n):
       a[i] = b[p[i]-1]
      return a

def genkeys(key,p10,p8):
   k = [0]*10
   k[:]=permute(p10,10,key)
   kl= lshift(k[0:5],1)
   kr= lshift(k[5:10],1)
   k1 = [0]*8
   k1=permute(p8,8,kl+kr)
   print('The generated key1 is: ')
   print(k1)
   kl[:]= lshift(kl,2)
   kr[:]= lshift(kr,2)
   k2 = [0]*8
   k2=permute(p8,8,kl+kr)
   print('The generated key2 is: ')
   print(k2)
   return k1,k2

def xor(k,k1):
   l = len(k1)
   res = [0]*l
   for i in range (l):
       res[i] = k[i]^k1[i]
   return res

def getval(s,a):
   row = str(a[0])+str(a[3])
   r = int(row,2)
   col = str(a[1])+str(a[2])
   c = int(col,2)
   res = [int(bit) for bit in bin(s[r][c])[2:]]
   return res
   

def fun(ep,k1,kl,kr,p4,s0,s1):
   k= [0]*8
   k = permute(ep,8,kr)
   k[:]= xor(k,k1)
   s=getval(s0,k[0:4])+getval(s1,k[4:8])
   v = permute(p4,4,s)
   return xor(v,kl)

   
def encrypt(ip,ep,k1,k2,s0,s1,p4,ipin,pt):
   k = permute(ip,8,pt)
   kl = k[0:4]
   kr = k[4:8]
   x = fun(ep,k1,kl,kr,p4,s0,s1)
   k[:] = kr + x

   kl[:] = kr
   kr[:]= x
   x[:] = fun(ep,k2,kl,kr,p4,s0,s1)
   return permute(ipin,8,(x+kr))

def decrypt(ip,ep,k1,k2,s0,s1,p4,ipin,ct):
   k = permute(ip,8,ct)
   kl = k[0:4]
   kr = k[4:8]
   x = fun(ep,k2,kl,kr,p4,s0,s1)
   k[:] = kr + x

   kl[:] = kr
   kr[:]= x
   x[:] = fun(ep,k1,kl,kr,p4,s0,s1)
   return permute(ipin,8,(x+kr))
   

p10 =[3,5,2,7,4,10,1,9,8,6]
p8=[6,3,7,4,8,5,10,9]
ip = [2,6,3,1,4,8,5,7]
ipin =[4,1,3,5,7,2,8,6]
ep=[4,1,2,3,2,3,4,1]
s0 =[[1,0,3,2],[3,2,1,0],[0,2,1,3],[3,1,3,2]]
s1=[[0,1,2,3],[2,0,1,3],[3,0,1,0],[2,1,0,3]]
p4 =[2,4,3,1]
pt = list(map(int, input("enter 8 bit plain text: ").split())) 
key = list(map(int, input("enter 10 bit key: ").split())) 
k1,k2 = genkeys(key,p10,p8) 
ct = encrypt(ip,ep,k1,k2,s0,s1,p4,ipin,pt)
print('The cipher text is: ')
print(str(ct))
dec = decrypt(ip,ep,k1,k2,s0,s1,p4,ipin,ct)
print('The original text is: ')
print(str(dec))