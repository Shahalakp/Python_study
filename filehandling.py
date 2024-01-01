# f=open("phonebook.py")
# print(f.read())

f=open("phonebook.py","r")
# print(f.read())
# print(f.readline(5))
# print(f.readline())
print(f.readlines(5))
f=open("phonebook.py","w")
print(f)

