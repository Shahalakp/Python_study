lis1=[0,1,2,3,4,5,6,">6"]
lis2=[]
flag=0
for i in lis1:
    val=int(input(f"provide the number of houses with {i} occupancy:   "))
    if val<0:
        print("input valid house number.")
        flag=1
        break
    else:
        lis2.append(val)
# print(lis2)
per=[]
for i in lis2:
    res=round((i/35)*100,2)
    per.append(res)
print(per)
if flag==0:
    print("occupants   ", *lis1,sep="\t")
    print("no.dwellings", *lis2,sep="\t")
    # print("percentage  ", *per, sep="%\t")
    for i in per:
        print(i,sep="%\t")