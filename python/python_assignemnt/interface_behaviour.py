'''

##?? 1] Use the abc module to create an abstract class.

##?? 2] Define abstract methods that must be implemented by subclasses.
'''

from abc import ABC, abstractmethod

class Readable(ABC):
    @abstractmethod
    def read(self):
        pass

class EBook(Readable):
    def read(self):
        return "Reading eBook" 

class Magazine(Readable):
    def read(self):
        return "Reading Magazine"
    
ebook = EBook() 
magazine = Magazine() 
print(ebook.read())
print(magazine.read())
