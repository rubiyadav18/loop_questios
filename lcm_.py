num=int(input("enter a first number"))
num1=int(input("enter a second number"))
for i in range(1,int(num/2)):
    if num%i==0 and num1%i==0:
        gcd=i
lcm=num,num1/gcd
print("gcd num and num1 gcd")