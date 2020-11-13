user=int(input("enter a number"))
guess=int(input("enter a number"))
while user!=guess:
    break
if guess>user:
    print("apka guess shi hai")
if guess<user:
    print("apka guess galat hai")
else:
    print("try again")