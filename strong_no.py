
i=int(input("enter a number"))
fact=1
sum=0
while fact<=i:
    if i//fact==0:
        fact=fact*i      
        i=i+1
        sum=sum+fact
        i=i//10
    if sum==fact:
        i=i+1
        print("strong num")
    else:
        print("not strong num")
    

