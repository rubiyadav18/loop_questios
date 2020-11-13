num=int(input("enter a number"))
user=num
sum=0
while num>0:
    i=1
    fac=1
    rem=num%10
    while i<=rem:
        fac=fac*i
        i=i+1
    sum=sum+fac
    num=num//10
    # print(sum)
    if sum==user:
        print("it is stronh num")
    else:
        print("it is not strog num")     