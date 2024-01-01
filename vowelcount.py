wrd=input("enter the sentence:")
vowel=["a","e","i","o","u"]
count=0
for i in wrd:
    if i in vowel:
        count+=1
print(count)