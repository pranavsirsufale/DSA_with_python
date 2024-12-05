# Write a python program to create a set.

'''
# Creating a set using curly braces
my_set = {1, 2, 3, 4, 5}

# Creating a set using the set() constructor
another_set = set([6, 7, 8, 9, 10])

# Printing the sets
print("Set created using curly braces:", my_set)
print("Set created using set() constructor:", another_set)

'''


# Write a Python program to add member(s) to a set.

'''
# Creating a set
my_set = {1, 2, 3}

# Adding a single element using add()
my_set.add(4)
print("Set after adding 4:", my_set)

# Adding multiple elements using update()
my_set.update([5, 6, 7])
print("Set after adding 5, 6, 7:", my_set)

'''


# Write a Python program to delete member(s) to a set.

'''
# Creating a set
my_set = {1, 2, 3, 4, 5}

# Using remove() to delete an element
my_set.remove(3)
print("Set after removing 3:", my_set)

# Using discard() to delete an element (no error if element is missing)
my_set.discard(2)
print("Set after discarding 2:", my_set)

# Using pop() to remove a random element
removed_element = my_set.pop()
print(f"Set after popping an element: {my_set}, Removed element: {removed_element}")

# Using clear() to remove all elements
my_set.clear()
print("Set after clearing all elements:", my_set)

'''


#Write a Python program to calculate the distance between the points (x1, y1) and (x2, y2).

'''
import math
def calculate_distance(x1, y1, x2, y2):
    # Calculate the distance using the distance formula
    distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    return distance

# Example usage
x1, y1 = 1, 2
x2, y2 = 4, 6

distance = calculate_distance(x1, y1, x2, y2)
print(f"Distance between ({x1}, {y1}) and ({x2}, {y2}) is: {distance}")

'''
