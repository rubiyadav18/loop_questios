n=100
i=0
a=0
while i<=n:
    j=1
    sum=0
    while j<=i:
        d=a%10
        sum=sum+d
        a=a//10
        a=a+1
        j=j+1
    if sum%9==0:
        print(sum,"s")
    i=i+1
# the number whose even divides by 9  
# this is strange number