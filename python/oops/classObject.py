#//!  Class and object

# creata Car class with attributes like brand and model. then create an instance of this class


# Q2 > Create an ElectricCar class that inherits from the Car class and has an additional attribute battery size

class Car:
    def __init__(self,model,brand):
        self.model = model
        self.brand = brand

    def full_name(self):
        return f"{self.brand} and {self.model}"




class ElectricCar(Car):
    def __init__(self,brand,model,fuel_type):
        super().__init__(brand,model)
        self.fuel_type = fuel_type
        


    def getCarDetails(self):
        
        return f'model is : {self.model}  , brand is : {self.brand} , fuel type is : {self.fuel_type}'




# objectOfCar = Car('s3','tata')
objectElectric = ElectricCar('s4','tata nexon','electric charge')




print(objectElectric.getCarDetails()   )










