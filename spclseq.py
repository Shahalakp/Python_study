import re
a="apple is red"
# regex=re.findall("\Aapp",a)
# regex=re.findall("d\Z",a)
# regex=re.findall("\Aapp",a)
# regex=re.findall(r"\bi",a)
# regex=re.findall(r"d\b",a)
# regex=re.findall(r"\Bed",a)
# regex=re.findall(r"app\B",a)
# regex=re.findall(r"\d",a)
# regex=re.findall(r"\D",a)
# regex=re.findall(r"\w",a)  #space is not recognized
# regex=re.findall(r"\W",a)
# regex=re.findall(r"\s",a)
regex=re.findall(r"\S",a)








print(regex)