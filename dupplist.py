num=[1,2,1,1,2,3,2,1,3,4,56,4,3,2,1,56]
res=[]
for i in num:
    if i not in res:
        res.append(i)

print(res)

