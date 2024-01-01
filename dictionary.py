a={"name":"shahala","age":23,"course":"b.tech"}
print(type(a))
print(a)
print(a["name"])
a["name"]="shahala kp"
print(a)

for i in a:
    print(i)
    print(a[i])

a["phone"]=6382941973
print(a)

d={"sivadath":{"name":"sivadath","phone":987765432,"email":"siva@123gmail.com"}}
# print(d["sivadath"])
val=d["sivadath"].values()
lis=list(val)
print(lis)
# print(type(val))
# print(val["name"])
