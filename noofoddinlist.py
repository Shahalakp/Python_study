num=[1,2,1,1,2,3,2,1,3,4,56,4,3,2,1,56]
count=0
new=[]
for i in num:
    if i%2!=0:
        if i not in new:
            new.append(i)
        #count+=1
#print(count)
print(new)

for i in new:
    count+=1
print(count)



