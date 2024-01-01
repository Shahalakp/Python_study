# n=int(input("ent the nmbr:"))
# input=n
# arm=0
# while n>0:
#     num=n%10
#     arm=arm+(num**3)
#     n=n//10

# if arm==input:
#     print("arms")
# else:
#     print("not")

# n=int(input("ent the nmbr:"))
# for i in range(2,n+1):
#     for j in range(2,i-1):
#         if i%j==0:
#             break
#     else:
#         print(i)

# num=[1,2,1,1,2,3,2,1,3,4,56,4,3,2,1,56]
# new=[]
# for i in num:
#     if i not in new:
#         new.append(i)
# print(new)
# new=[i for i 
from functools import reduce
a=[2,5,7,346,98,56]

# def sq(num):
#     return num**2
# b=[]
# for i in a:
#     b.append(sq(i))

# print(b)
b=list(map(lambda num:num**2,a))
print(b)

# def even(num):
#     if num%2==0:
#         return num

# res=list(filter(even,a))
# print(res)

# res2=list(map(lambda x:x*2,li))
# print(res2)


sum=reduce(lambda tot,num:tot+num,a)
print(sum)
# res3=reduce(lambda x,y:x+y,li)
# print(res3)