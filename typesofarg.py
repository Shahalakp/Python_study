# positional arg:
def fun1(a,b):
    print(a)
    print(b)
fun1(11,21)

# arbitrary arg:
def fun2(a,b,*c):
    print(a)
    print(b)
    print(c)
fun2(10,20,30,40,50)

# keyword arg:
def fun1(a,b):
    print(a)
    print(b)
fun1(b=11,a=21)


# arbitrary keyword arg:
def fun3(a,**b):
    print(a)
    print(b)
fun3(b=22,a=33,c=44)

# default parameter
def fun1(a,b=0):
    print(a)
    print(b)
fun1(11)

