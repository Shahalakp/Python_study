class Laptop():
    def __init__(self,brnd,ram,rom):
        self.Brand=brnd
        self.RAM=ram
        self.ROM=rom
    def Display_ram(self):
        print(f"RAM value of {self.Brand} is:{self.RAM}")
    def Display_rom(self):
        print(f"ROM value of {self.Brand} is:{self.ROM}")

ob=Laptop("Lenovo ThinkPad P16","128GB","256GB")
ob.Display_ram()
ob.Display_rom()

oc=Laptop("hp","8GB","256GB")
oc.Display_ram()
oc.Display_rom()
    