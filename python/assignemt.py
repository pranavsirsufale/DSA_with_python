import math


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






    







