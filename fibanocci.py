n=int(input("enter the number:"))
num1=0
num2=1
count=2
print(0)
print(1)
#while count<n:
for count in range(n):
    next=num1+num2
    print(next)
    num1=num2
    num2=next
    count+=1
