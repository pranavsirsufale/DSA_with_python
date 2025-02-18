'''
###?? 1 ] Create multiple base classes.

###?? 2 ] Derive a class that inherits from all base classes.
'''
class Animal:
    def speak(self):
        print('Animal speaks')


class Bird:
    def fly(self):
        print('Bird flies')

class Sparrow(Animal,Bird):
    def chirp(self):
        print('Sparrow chirps')


sparrow = Sparrow()
sparrow.speak()
sparrow.fly() 
sparrow.chirp() 


