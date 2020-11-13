n=input("enter a number")
i=0
a=0
while(i<len(n)):
    j=0
    b=1
    while(j<len(n)):
        b=b*int(n[i])
        j=j+1
    a=a+b
    i=i+1
c=int(n)
if(c==a):
    print("it is strong number")
else:
    ptint("not strong num")