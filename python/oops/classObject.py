#//!  Class and object

# creata Car class with attributes like brand and model. then create an instance of this class


# Q2 > Create an ElectricCar class that inherits from the Car class and has an additional attribute battery size


# Q3 >>> Encapsulation   ( USING DUNDER OPERATOR CAN MAKE ATTRIBUTES PRIVATE (ENCAPSULATE WITHIN CLASS))
# //? APPNE CLASS KE ANDAR TO ACCESS HO PAR BAHAR ACCESS NA HO 
# >>>> Modify the car class to encapsulate the brand attribute, making it private, and provide a getter method for it.

 

# Q4 >>> POLIMORPHISM 
#//! Q ) Demonstrate polymorphism by defining a method fuel_type in both Car and ElectricCar classes , but with different behaviours.






class Car:
    def __init__(self,model,brand):
        self.__model = model
        self.__brand = brand


    def get_brand(self):
        return self.__brand + ' this is brand'


    def full_name(self):
        return f"{self.__brand} and {self.__model}"


class ElectricCar(Car):
    def __init__(self,brand,model,fuel_type):
        super().__init__(brand,model)
        self.fuel_type = fuel_type
        

    # We CANNOT ACCESS __MODEL AND __brand BECAUSE THEY ARE PRIVATE 
    def getCarDetails(self):
        # return f'model is : {self.__model}  , brand is : {self.__brand} , fuel type is : {self.fuel_type}'
        return f"fuel is {self.fuel_type}"



objectOfCar = Car('s3','tata')
objectElectric = ElectricCar('s4','tata nexon','electric charge') 


print(objectElectric.getCarDetails()   )










