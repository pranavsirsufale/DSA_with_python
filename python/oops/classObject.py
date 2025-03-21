#//!  Class and object

# creata Car class with attributes like brand and model. then create an instance of this class


# Q2 > Create an ElectricCar class that inherits from the Car class and has an additional attribute battery size


# Q3 >>> Encapsulation   ( USING DUNDER OPERATOR CAN MAKE ATTRIBUTES PRIVATE (ENCAPSULATE WITHIN CLASS))
# //? APPNE CLASS KE ANDAR TO ACCESS HO PAR BAHAR ACCESS NA HO 
# >>>> Modify the car class to encapsulate the brand attribute, making it private, and provide a getter method for it.

 

# Q4 >>> POLIMORPHISM 
#//! Q ) Demonstrate polymorphism by defining a method fuel_type in both Car and ElectricCar classes , but with different behaviours.


 
#??!  Car count


#??? > STATIC METHOD
#???! add a static method to the Car class that returns a general description of a car 


#?? > Create Multiple Inheritance 
#! Create two classes Battry and Engine . and let the ElectricCar inherit from both, demonstraing multiple inheritence



#?? A static methods is a method that belongs to a class rather than an instance of a class.

class Car:
    car_count = 0 
    def __init__(self,model,brand):
        self.__model = model
        self.__brand = brand
        Car.car_count += 1

    def get_brand(self):
        return self.__brand + ' this is brand'


    def full_name(self):
        return f"{self.__brand} and {self.__model}"


    def fule_type(self):
        return 'Petrol'
    

    # this is static methods 
    @staticmethod
    def general_description():
        return 'cars are means of transport '


    #//? makes the property read only and the method will act like a variable but  read only
    @property
    def model(self):
        return self.__model


class ElectricCar(Car):
    def __init__(self,brand,model,fuel_type):
        super().__init__(brand,model)
        self.fuel_type = fuel_type


    def fuel_type():
        return "Electric Charge"
        

    # We CANNOT ACCESS __MODEL AND __brand BECAUSE THEY ARE PRIVATE 
    def getCarDetails(self):
        # return f'model is : {self.__model}  , brand is : {self.__brand} , fuel type is : {self.fuel_type}'
        return f"fuel is {self.fuel_type}"
    



objectOfCar = Car('s3','tata')
objectElectric = ElectricCar('s4','tata nexon','electric charge') 


# print(objectElectric.getCarDetails()   )
# print(objectOfCar.general_description())
# print(Car.general_description())
# print(objectOfCar.model)



class Battery:
    def battery_info(self):
        return "this is battery"

class Engine:
    def engine_info(self):
        return "this is engine"


class ElectricCarTwo(Battery,Engine,Car):
    pass


my_new_tesla = ElectricCarTwo('tesla','Model S')
    

print(my_new_tesla.engine_info())

    