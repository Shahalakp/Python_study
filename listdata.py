a=[1,2,3,"apple"]
print(a)
a[2]="kiwi"
print(a)
# print(a[2:4])
# print(a[0:])
# print(a[::-1])

a.append("cherry")
print(a)
res=a.pop(2)
print(res)
print(a)
b=[4,"banana"]
a.extend(b)
print(a)
a.insert(2,"7")
print(a)
a.remove("cherry")
print(a)
a.reverse()
print(a)

print(a.index("banana"))
c=[1,23,3,45,209]
c.sort()
print(c)

c.sort(reverse=True)
print(c)

d=[1,2,"cherry","banana"]
print(d)
d.reverse()
print(d)