# r=0
# while r<=4:
#     c=0
#     while c<=2:
#         if (c==0) or (r==0) and (c==2) or (r==1) and (c==1) or (r==3) and (c==1) or (r==4) and (c==2):
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#         c=c+1
#     print()
#     r=r+1
# i=1
# while i<=10:
#     j=1
#     while j<=i:
#         print(i,end=" ")
#         j=j+1
#     print()
#     i=i+1
# a=1
# c=1
# while a<5:
#     for i in range(a):
#         print(c,end=" ")
#         c=c+1
#     print()
#     a=a+1
a=1
c=1
while a<5:
    b=0
    while b<a:
        print(c,end=" ")
        c=c+1
        b=b+1
    print()
    a=a+1