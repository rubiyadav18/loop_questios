a=int(input("enter a number"))
b=2
c=0
while b<a:
    if a%b==0:
        c=c+1
    b=b+1
if c==0:
    print("prime")
else:
    