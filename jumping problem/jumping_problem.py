def make_jump(ar):
    if len(ar) == 0:
        return False
    destination = len(ar) - 1
    position = destination
    while position >= 0:
        if position == destination:
            position -= 1
            continue
        if position + ar[position] >= destination:
            destination = position
        position -= 1
    if destination == 0:
        return True
    return False

arr = [2, 1, 3, 1, 2]
arr2 = [2, 0, 0, 1, 3]
arr3 = [3, 8, 9, 0, 1, 3]
arr4 = [3 , 2, 1 , 0 , 7]
arr5 = [3 , 2, 1 , 1 , 7]
arr6 = [ 1 , 1, 2, 5 , 2, 1, 0 , 0 , 1 , 3]

print(make_jump(arr))   
print(make_jump(arr2)) 
print(make_jump(arr3)) 
print(make_jump(arr4)) 
print(make_jump(arr5)) 
print(make_jump(arr6)) 
'''
#! OUTPUT 
#? True
#? False
#? True
#? False
#? True
#? True
'''






#++++++++++++++++++++++
'''
def check_even_odd(n):
    if n % 2 == 0 :
        return 'even'
    else :
        return 'odd'


print(check_even_odd(19))


'''



'''
# 1 , 4 ,9 , 16 , 25 

def check_perfect_square(n):
    start = 1 
    sroot = 1
    if n == 1 :
        return '1'
    while sroot < n:
        sroot = start * start 
        if sroot == n:
            return 'perfect square'
        if sroot < n :
            start += 1
    return 'unperfect square'


print(check_perfect_square(1))

'''