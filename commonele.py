a=[1,3,2,4,65,7,90]
b=[2,3,44,5,7,90,78]
c=[]
for i in a:
    # if i in b:
    for j in b:
        if i==j:
            c.append(i)
print(c)

