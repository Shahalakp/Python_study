f=open("alanturing.txt","r")

word=f.read()
res=word.split()
# print(res)
# word=f.split()
# print(word)

dict={}
for i in res:
    if i in dict:
        dict[i]+=1
    else:
        dict[i]=1
print(dict)