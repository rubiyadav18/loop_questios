a=int(input("enter a number"))
num=a
sum=0
c=len(str(a))
i=0
while i<c:
    b=(a%10)**c
    sum=sum+b
    a=a//10
    i=i+1
if num==sum:
    print("it is amstronh number")
else:
    print("it is not amstronh number")