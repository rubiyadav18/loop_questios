# i=int(input("enter a number"))
# # x=1
# rev=0
# while i>0:
#     rev=rev*10+i%10
#     i=i//10
#     print("revers=",rev)
# if x==b:
#     print("yes")
# else:
#     print("no")
# i=int(input("enter a number"))
# rev=0
# x=0
# while i>0:
#     rev=rev*10+i%10
#     i=i//10
# if x==rev:
#     print("yes")
# else:
#     print("no")
i=int(input("enter a number"))
x=i
rev=0
while i>0:
    rev=rev*10+i%10
    i=i//10
    if x==rev:
        print("palidrom number")
else:
        print("it is not")
                
