import math
# Q 1) Write a python program to accept the radius from the user and print area of the circle?

# area of circle Pi * r ^2


def area_of_circle(r):
    return ((math.pi) * (r**2))

radiusofcircle = float(input('enter the area of radius : '))

print(area_of_circle(radiusofcircle))
