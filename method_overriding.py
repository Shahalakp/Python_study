class main:
    def __init__(self,a):
        print("object created")
    def fun(self):
        print("parent method")

class child(main):
    def __init__(self):
        print("bhjzbfj")
    def fun(self):
        print("child method")
        # super().fun()

obj=child()
obj.fun()

#private Specifier
class Main:

    __name="main"
    def main_meth(self):
        print(self.__name)
ob=Main()
ob.main_meth()