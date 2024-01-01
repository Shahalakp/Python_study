
def factorial(n):
    fact=1
    if n<0:
        print("invalid number.")
    elif n==0:
        print("factorial is 1")
    else:
        for i in range(n,0,-1):
            fact=fact*i
        return fact

num=int(input("enter the number:"))  
print(factorial(num))

