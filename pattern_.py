i=1
while i<=5:
    j=5
    while j>=i:
        print("*"*i,end="")
        print(""*j,end="")
        print()
        j=j-1
        i=i+1