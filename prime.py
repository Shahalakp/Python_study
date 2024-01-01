a=int(input("enter the number"))
flag=0
if a==1:
    print("it is a prime")
elif a==2:
    print("it is a prime")
else:
    for i in range(2,a+1):
        if i%a==0:
            #print("it is not prime")
            flag=1
if flag==0:
    print("it is prime")
else:
    print("it is not a prime")

    