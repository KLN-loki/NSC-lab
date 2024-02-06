import sympy
p=sympy.randprime(2,1000)
a=sympy.primitive_root(p)
pri_a=int(input("Enter the private key of A:"))
pri_b=int(input("Enter the private key of B:"))
ya=pow(2,pri_a,389)
yb=pow(2,pri_b,389)
print(ya,yb)

sec_a=pow(yb,pri_a,389)
sec_b=pow(ya,pri_b,389)
print(p,a)
print("Secret key A:",sec_a)
print("Secret key B:",sec_b)

if sec_a==sec_b:
    print("The keys are exchanged symmetrically")
else:
    print("The keys are not exchanged symmetrically ")