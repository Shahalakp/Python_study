class Student:
    def __init__(self,name,rno,clss):
        #instance variable
        # print(self)
        self.Name=name
        self.RollNo=rno
        self.Class=clss
    def __str__(self):
         return "object"
        # return self.Name
    #class variable
    center="calicut"
    # def display(self):
    #     print(self)
    #     print(self.Name)

    def __del__(self):
        print(f"{self.Name} object destructed.")
ob=Student("ajith","23","bsc cs")
print(ob)
# ob.display()
# print(ob.Name)

oc=Student("shahala","14","b.tech")
print(oc)
# oc.display()
# print(oc.Name)
# print(ob.RollNo)