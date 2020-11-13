i=int(input("enter a number"))
count=0
while i>0:
    i=i//10
    count=count+1
print("count of digit=",count)