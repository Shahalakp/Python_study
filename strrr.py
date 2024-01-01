a="apple is red"
print(a[5])
print(a[-3])
b="shahala"
c="sha@123"
msg="hi %s, welcome to luminar. your account id is:%s"%(b,c)
d="wafa"
e="wafa@234"
msg2="hi {}, welcome to luminar, your account id is:{}".format(d,e)
msg3=f"hi {d}, welcome to luminar, your account id is:{e}"
print(msg3)


#escape charecter
i="apple is \nred"
j="apple is r\ted"
f="apple is r\bed "
g="\\new apple is red"
h=r"C:\Users\hp\OneDrive\Desktop\pythonexamples\printprimes.py"
print(h)
print(g)
print(f)
print(i)
print(j)
k="she sells sea shells on tne sea shore"
#slic=k[4:9]
#slic=k[::-1] #reverse the string(it add -1 to 0 index)
#slic=k[-6:-1]
slic=k[::2]  #add 2 to 0 index when :: given
print(slic)

#mutable-list,set,dict
#immutable-int,float,bool,tuple,string