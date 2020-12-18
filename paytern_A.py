r=0
while r<=4:
    c=0
    while c<=3:
        if c==0 or c==3 or (r==0 and c!=0 and c!=3) or (r==2 and c!=0 and c!=3):
            print("*",end=" ")
        else:
            print(" ",end=" ")
        c=c+1
    print()
    r=r+1