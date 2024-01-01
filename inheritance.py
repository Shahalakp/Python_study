#single inheritance
class A:  #parent class/super class
    name="name is A"
    def fun(self):
        print("method of A")

class B(A):  #child class/subclass
    # pass
    def display(self):
        print(super().name)
        super().fun()

b=B()
# print(b.name)
# b.fun()
b.display()

#multiple inheritance

class MA:
    ma="member of MA"

class MB:
    mb="member of MB"

class C_of_AB(MA,MB):
    pass

childclass=C_of_AB()
print(childclass.ma)
print(childclass.mb)
    

 #multilevel inheritance

class Baseclass:
    name="shahala"   

class child1(Baseclass):
    cname="shalu"

class grand_child(child1):
    pass


obj=child1()
print(obj.name)

obj2=grand_child()
print(obj2.cname)


#heirarchical inheritance:

class parent:
    msg="present in grand parent class"

class c1(parent):
    msg="c1 msg"

class c2(parent):
    msg="c2 msg"

ob=c2()


