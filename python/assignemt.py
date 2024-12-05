import math
import calendar
from datetime import date
import os
import subprocess
import socket


# Q 1) Write a python program to accept the radius from the user and print area of the circle?

# area of circle Pi * r ^2

'''
def area_of_circle(r):
    return ((math.pi) * (r**2))

radiusofcircle = float(input('enter the area of radius : '))

print(area_of_circle(radiusofcircle))

'''


#Write a python program to calculate the area of a square
# formulat side * side

def area_of_square(side):
    return (side*side)


'''
side = float(input('enter length of the side : '))

print(area_of_square(side))

'''

#Write a python program to calculate the area of rectangle
# area of rectangle = side * length



'''
def area_of_rectangle(width,length):
    return (width*length)
'''

# Write python program to perform declare positive values but print negative values

'''
def pos_to_neg(positive_number):
    return  -positive_number
n_number = 65466
# print(pos_to_neg(n_number))
neg_val = pos_to_neg(n_number)
print(neg_val + 2)
'''


#Write a python program for calculate the factorial of a number using a for loop.

'''
def calculate_factorial(n):
    facto = 1
    for i in range(1,n+1):
        facto *= i
    return facto
print(calculate_factorial(5))
'''



# Write a python program to generate the Fibonacci series up to N terms.

# feboo = 0 1 1 2 3 5 8 13 21 34

'''
def fiboo(number_of_terms):
    array = [0,1]
    for i in range(number_of_terms-2):
        array.append(array[i] + array[i+1])
    return array
print(fiboo(10))
'''



# Write a python program for Check if a number is prime using for loop.


'''
def check_prime(n):
    if n <= 1:
        return f'{n} : is Prime number'
    till = (int(n**0.5)) + 1
    for i in range(2,till):
        if n % i == 0:
            return f'{n} : is not a Prime number'
    return f'{n} : is a Prime number'
print(check_prime(3))
'''



# Write a python program to Calculate the sum of digits of a number using a while loop.
'''
def calculate_sum(digit):
    digit = str(digit)
    sum=i = 0
    while i < len(digit):
        sum += float(digit[i])
        i += 1
    return sum
digit = 1234569 # 21
print(calculate_sum(digit))
'''

#Write a python program for reverse a given number using a while loop.


'''
def reverse_number(n):
    # n = [i for i in str(n)]
    # second_pointer = len(n)-1
    # print(n)
    # for i in range(int(len(n)/2)):
    #     n[i],n[second_pointer] = n[second_pointer],n[i]
    #     second_pointer -= 1
    # return n
    reversed_number = 0
    while n > 0 :
        last_digit = n % 10
        reversed_number = (reversed_number * 10 ) + last_digit
        n //= 10
    return reversed_number 
number = 13132
rev_num = reverse_number(number)
print(rev_num)

'''


# Write a python program for Check if a number is prime using for loop.

'''
def check_is_prime(n):
    if n <= 1:
        return f"{n} : is not a prime number"
    till = int(n**0.5) + 1
    for i in range(2,till):
        if n % i == 0 :
            return f'{n} : is not a prime number'
    return f'{n} : is a prime number'
print(check_is_prime(7))

'''
    


# Write a python program computes the length of a list using recursion


'''
listt = [165, 6, 1, 61, 6, 1, 61, 1, 651, 16516]

def find_length(n):
    try:
        # Try to access the nth element
        listt[n]
        # If successful, continue recursion
        return find_length(n + 1)
    except IndexError:
        # Return the current index when IndexError is raised
        return n
# Example usage
print(find_length(0))  # Output: 10

'''


# print extentation of file 
'''
filename = 'something.txt'
def print_ext(finematwithextentaion):
    return finematwithextentaion[finematwithextentaion.index('.')+1:]
print(print_ext(filename))
'''


# Write a python program that prints the calendar for a given month and year. Note : use 'calendar' module. 

'''
def print_calendar(year,month):
    print(calendar.month(year,month))
print_calendar(2024,12)
'''


# Write a python program to calculate the number of days between two dates. Sample dates: (2014, 7, 2), (2014, 7, 11)


'''
def calculate_days_between(date1, date2):
    d1 = date(*date1)
    d2 = date(*date2)
    delta = d2 - d1
    return abs(delta.days) 


date1 = (2014, 7, 2)
date2 = (2014, 7, 11)


days_between = calculate_days_between(date1, date2)
print(f"Number of days between {date1} and {date2}: {days_between}")
'''




#Write a python program that prints out all colors from color_list_1 that are not present in color_list_2.
'''
Test data :
color_list_1 = set(["white", "black", "red"])
color_list_2 = set(["red", "green"]) 
expected output :
{'black', 'white'}
'''

'''
color_list_1 = set(["white", "black", "red"])
color_list_2 = set(["red", "green"]) 

print(set.difference(color_list_1,color_list_2))

for i in color_list_1:
    if i not in color_list_2:
        print(i)

'''


# area of triangle 
'''
def area_of_triangle(base,height):
    return (0.5)* (base) * (height)
print(area_of_triangle(10,15))
'''


#Write a python program to check whether a file exists.

'''
def check_path_exists(path):
    if os.path.exists(path):
        return 'File exists'
    else:
        return 'File does not exist'

address = 'F:/DSA/practical/python'
path = r'F:/DSA/practical/python/area_of_circle.py'
print(check_path_exists(path))
'''

# Write a python program that calls an external command.

'''

def run_command(command):
    try:
        # Run the command and capture the output
        result = subprocess.run(command, shell=True, check=True, text=True, capture_output=True)
        
        # Print the command output
        print("Command output:", result.stdout)
        print("Command error (if any):", result.stderr)
    except subprocess.CalledProcessError as e:
        print(f"Command failed with error: {e}")

# Example usage
command = 'echo Hello, World!'  # You can replace this with any command you want to run
run_command(command)

'''



# Write a python program to retrieve the path and name of the file currently being executed.

'''
print(os.path.abspath(__file__))
print(__file__)
print(os.path.dirname(__file__))
print(os.path.basename(__file__))
'''


# Write a python program to find local ip addresses using python's stdlib.

'''
hostname = socket.gethostname()
# Get the local IP address associated with the hostname
print(socket.gethostbyname(hostname))
local_ip = 0

print(local_ip)

'''




# Write a python script to sort (ascending and descending) a dictionary by value


'''
def sort_dict_by_value(d, ascending=True):
    sorted_dict = dict(sorted(d.items(), key=lambda item: item[1], reverse=not ascending))
    return sorted_dict


my_dict = {'apple': 5, 'banana': 2, 'cherry': 10, 'date': 7}


sorted_dict_asc = sort_dict_by_value(my_dict, ascending=True)
print("Sorted Dictionary (Ascending):", sorted_dict_asc)

sorted_dict_desc = sort_dict_by_value(my_dict, ascending=False)
print("Sorted Dictionary (Descending):", sorted_dict_desc)
'''











    







