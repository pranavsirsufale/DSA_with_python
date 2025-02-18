'''

#? 1 ] Compare the middle element with the target.

#? 2 ] If the middle element is equal to the target, return its index.

#? 3 ] If the target is smaller than the middle element, search the left half.

#? 4 ] If the target is greater, search the right half.
'''

def binary_search(arr,target):
    low = 0 
    high = len(arr) -1 

    while low <= high:
        mid = (low + high ) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid
        else :
            high = mid -1 
    return 1

# Example usage
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
result = binary_search(arr, 4)
print(result)
