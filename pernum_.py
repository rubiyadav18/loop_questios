# n=int(input("enter a number"))
# sum1=1
# i=1
# for i in range(1,n):
#     if n%i==0:
#         sum1=sum1+1
# if sum1==n:
#     print("it is perfect number")
# else:
#     print("it is not perfect number")
n=int(input("enter a number"))
sum=1
i=1
for i in range(1,n):
    if n%i==0:
       sum=sum+1
if sum==0:
    print("it is perfect number")
else:
    print("it is not perfect number")
