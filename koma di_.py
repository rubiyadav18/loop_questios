num=int(input("enter a number"))
b=2
while b<num:
    if num%b==0:
        print("it is not prime num")
        break
    b=b+1
else:
    print("it is  prime num")