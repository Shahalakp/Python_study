n=int(input("enter the number:"))
# rem=0
# if n==1 or n==2:
#     if n==1:
#         print(n)
#     else:
#         for i in range(n,0,-1):
#             print(i)
# elif n<=0:
#     print("invalid number")
# else:
#     for i in range(3,n+1):
#         for j in range(i-1,1,-1):
#             rem=i%j
#             if rem!=0:
#                 print(i)
# if n<=0:
#     print("invalid number")
# elif n==1 or n==2:
#      if n==1:
#         print(n)
#      else:
#          print(1)
#          print(2)
# else:
#     print(1)
#     print(2)
#     for j in range(2,n+1):
#         for i in range(2,j+1):
#             if i%j==0:
#                 #print("it is not prime")
#                 rem==1
#         if rem==0:
#             print(j)

for i in range(1,n+1):
        for j in range(2,i):
            if i%j==0:
                break
        else:
            print(i)           
