# i=1
# while i<=5:
#     j=5
#     while j>=5:
#         print("5"*i,end="")
#         print(""*j,end="")
#         print()
#         j=j-1
#         i=i+1
i=int(input("enter a number amstromh number"))
a=i
sum=0
while i>0:
    sum=sum+(i%10)*(i%10)*(i%10)
    i=i//10
    if a==sum:
        print("it is amstromg number")
else:
        print("it is not amstrong")
    