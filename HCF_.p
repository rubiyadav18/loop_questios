n=int(input("enter a number"))
y=int(input("enter a number"))
i=1
c=0
while i<=y:
    if n%i==0 and y%i==0:
        print("HCF",i)
        i=i+1
        c=i
        print("HCF",c)