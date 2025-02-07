#//!  Class and object

# creata Car class with attributes like brand and model. then create an instance of this class

class Car:
    def __init__(self,model,brand):
        self.model = model
        self.brand = brand

    def full_name(self):
        return f"{self.brand} and {self.model}"


objectOfCar = Car('s3','electric')

print(objectOfCar.full_name()   )










