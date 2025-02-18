
'''
##?? 1 ] Define an abstract class to act as an interface.

##?? 2 ] Ensure subclasses implement the required methods.
'''
from abc import ABC,abstractmethod

class Readable(ABC):
    @abstractmethod
    def read(self):
        pass


class Ebook(Readable):
    def read(self):
        return('Reading E-book ')


class Magazine(Readable):
    def read(self):
        return('Reading Magazine')

ebook = Ebook() 
magazine = Magazine() 
print(ebook.read())
print(magazine.read())
