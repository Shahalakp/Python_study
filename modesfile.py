# f=open("alanturing.txt","w")
# f.write("hi how are you")
f=open("alanturing.txt","a")
lst=["apple","is ","red"]
f.writelines(lst)

a=open("alan2.txt","w")
a.write("hi")

b=open("alan3.txt","x") #create a file in that name

f.close()
f=open("alanturing.txt")
print(f.read())



