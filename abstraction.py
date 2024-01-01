from abc import ABC,abstractmethod

class Car(ABC):
    @abstractmethod
    def accrelerate(self):
        pass
    def mileage(self):
        pass

class Honda(Car):
    name="honda"
    def indicator(self):
        print("indicating")
    def accrelerate(self):
        print("accelerating...")
    def mileage(self):
        print("mileage is 30")
