n=int(input("enter the number:"))
fact=1
if n<0:
    print("invalid number.")
elif n==0:
    print("factorial is 1")
else:
    #while n!=0:
    for i in range(n,0,-1):
        fact=fact*i
        #n-=1
    print(fact)   
