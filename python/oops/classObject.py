#//!  Class and object

# creata Car class with attributes like brand and model. then create an instance of this class

class Car:
    model = None
    brand = None

    def __init__(self,model,brand):
        self.model = model
        self.brand = brand



objectOfCar = Car('s3','electric')

print(objectOfCar.model   )










