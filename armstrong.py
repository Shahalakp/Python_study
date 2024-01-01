n=int(input("enter the number:"))
input=n
arm=0
while n>0:
    rem=n%10
    #a=rem**3
    #arm+=a
    arm=arm+(rem**3)
    n=n//10
if arm==input:
    print("it is a armstrong")
else:
    print("it is not an armstrong")

