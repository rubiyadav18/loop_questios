a=3
while a<=100:
    count=0
    b=2
    while b<a:
        if a%b==0:
            count=count+1
        b=b+1
    if count==0:
        print(a)
    a=a+1

