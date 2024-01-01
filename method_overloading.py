from multipledispatch import dispatch

@dispatch(int,int)
def add(a,b):
    print(a+b)


@dispatch(int,int,int)
def add(a,b,c):
    print(a+b+c)

add(10,20)
add(10,20,30)