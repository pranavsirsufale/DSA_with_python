# Write a python program to compute the future value of a specified principal amount, rate of interest, and number of years. Test data : amt = 10000, int = 3.5, years = 7 expected output : 12722.79

# F = p ( 1 + (r/100)) ** t
# future value = f
# p = principle value
# 1 

'''
'''
def calculate_future_value(principle,rate,year):
    return ((principle)*((1 + (rate/100) )** year) )
principle = 10000
rate = 3.5
year = 7
future_value = calculate_future_value(principle,rate,year)
print(future_value)
