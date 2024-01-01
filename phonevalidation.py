import re
num=input("enter the num:")
regex=re.findall("^[+]91[-]\d{10}$",num)
print(regex)