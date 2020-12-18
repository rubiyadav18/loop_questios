r=1
while r<=4:
    c=1
    while c<=4:
        if (r==c) or (c==1 and r!=1) or (c==3 and r!=3 and r!=4) or (c==2 and r!=2 and r!=3 and r!=4):
            print("*",end=" ")
        else:
            print(" ",end=" ")
        c=c+1
    print()
    r=r+1
