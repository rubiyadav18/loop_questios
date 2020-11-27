odd=1
for i in range(1,5):
    k=0
    for j in range(1+odd+1):
        if (j<=i):
            k=k+1
        else:
            k=k-1
        print(k,end="")
    print()
    odd=odd+2
            