import re
# a="apple is red"
# a="apple is not red impossible"
# res=re.search("i.*s",a)
# print(res)

# b="the rain spain"
# ex=re.search("^t.*spain$",b)
# print(ex)

s="the rain in spain"
# regex=re.search("in",s)
# regex=re.findall("i",s)
# regex=re.split(" ",s)
# regex=re.sub("i","*",s)
# regex=re.finditer("in",s)
# for i in regex:
#     print(i)
#     print(i.start())
#     print(i.group())
# #     print(i)
# print(regex)

# username=input("enter the username:")
password=input("enter the password:")
# regex=re.search("123",password)
regex=re.search("[a-zA-Z0-9]",password)
# email=input("enter the email id:")
# regex=re.search("[a-z0-9._#-]+[@][0-9a-z.]+[.][a-z]{2,3}$",email)
print(regex)
# if regex:
    # print("valid")
# else:
    # print("invalid")

# [a-z]
# [A-Z]
# [0-9]
# [a_zA_Z0-9]