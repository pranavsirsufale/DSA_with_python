'''
#? 1 ] Start from the first element and check if it's equal to the target.

#? 2 ] If it is, return the index.

#? 3 ] If it's not, move to the next element and repeat.
'''


def linear_search(arr,target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1


arr = [10, 20, 30, 40, 50]
result = linear_search(arr, 30)
print(result)