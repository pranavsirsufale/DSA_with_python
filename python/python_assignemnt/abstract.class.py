
'''
#?? 1 ] Use the abc module to define abstract methods.

#?? 2 ] Derived classes implement these abstract methods.
'''

from abc import ABC,abstractmethod

class Sharp(ABC):
    @abstractmethod
    def area(self):
        pass

class Rectangle(Sharp):
    def __init__(self,width,height):
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height
    

rectangle = Rectangle(5,4)
print(rectangle.area())