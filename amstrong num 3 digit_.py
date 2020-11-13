i=int(input("enter a number"))
a=i
sum=0
while i>0:
    c=(i%10)**3
    i=i//10
    sum=sum+c
if a==sum:
    print("it is amstrong number")
else:
    print("it is not amstrong number")