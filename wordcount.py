a="hi hello hi hello red hello red hi hi"
lis=list(a)
newlis=[]
finallist=[]
# print(lis)
stri=""
for i in lis:
    if i !=" ":
        newlis.append(i)
    else:
        for j in newlis:
            stri+=j
        finallist.append(stri)
        stri=""
        newlis.clear()
for j in newlis:
    stri+=j
finallist.append(stri)        
print(finallist)

wordlist=[]
for i in finallist:
    if i not in wordlist:
        wordlist.append(i)
print(wordlist)

countlist=[]
count=0
for i in wordlist:
    for j in finallist:
        if i==j:
            count+=1
    countlist.append(count)
    count=0
print(countlist)

res={}
for i in wordlist:
    for j in countlist:
        res[i]=j
        countlist.remove(j)
        break
print(res)



wrd=input("enter the sentence:")
word=wrd.split(" ")
print(word)

res={}
for i in word:
    if i in res:
        res[i]+=1
    else:
        res[i]=1
print(res)