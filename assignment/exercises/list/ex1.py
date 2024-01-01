# Given a list, write a Python program to swap first and last element of the list.


def newlist(li):
    size=len(li)

    new=li[size-1]
    li[size-1]=li[0]
    li[0]=new
    return li

li=[]
n=int(input("enter the no.of elements:"))

for i in range(0,n):
    a=input("enter the value:")
    li.append(a)
print(li)    

newli=newlist(li)
print(newli)