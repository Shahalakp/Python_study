sen=input("enter the sentence:")
res=sen.split(" ")
l=0
for i in res:
    if len(i)>l:
        l=len(i)
        word=i
print(word)
    