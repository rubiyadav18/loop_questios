# 1 2 3 4
# 9 10 11 12
# 13 14 15 16
# 5 6 7 8
# n = 4

# i have to slove in for  loop

# n=4
# empty_list=[]
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         if i==2:
#             empty_list.append(j+4)
#         elif i==1:
#             print(j,end=' ')
#         else:
#             print((i-1)*4+j,end=' ')
#     if j!=2:
#         print()
# for i in empty_list:
#          print(i,end=' ')


# 1 2 3 4 5
# 11 12 13 14 15
# 21 22 23 24 25
# 16 17 18 19 20
# 6 7 8 9 10

n=5
e=[]
for i in range(1,n+1):
    for j in range(1,n+1):
        if i==2:
            e.append(j+5)
        elif i==1:
            print(j,end=' ')
        else:
            print((i-1)*5+j,end=' ')
    if j!=3:
        print()
for i in e:
    print(i,end=' ')
    