n=int(input("enter a number"))
for rows in range(n,0,-1):
    for col in range(1,rows+1):
        print(col,end="")
    print()