import re
f=open("phone_numbers.txt","a")
num=input("enter the num:")
regex=re.findall("^[0-9]{10}$",num)

# print(type(regex))
if regex:
    f.writelines(num+"\n")
    print("valid")
else:
    print("invalid number")

