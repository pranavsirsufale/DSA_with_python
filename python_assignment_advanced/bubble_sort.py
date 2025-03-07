'''
### bubble sort
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0 , n - i -1 ):
            if arr[j] > arr[j+1]:
                arr[j] , arr[j+1] = arr[j+1],arr[j]
# Example usage
arr = [64, 34, 25, 12, 22, 11, 90]
bubble_sort(arr)
print(arr)       








def optimized_bubble_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        swapped = False
        for j in range(n - i - 1 ):
            if arr[j] > arr[j + 1 ]:
                arr[j] , arr[j+1] = arr[j+1] , arr[j]
                swapped = True
        if not swapped: #? No Swaps means already sorted
            break


# Example usage
arr = [5, 3, 8, 4, 2]
optimized_bubble_sort(arr)
print("Sorted Array:", arr)

'''




def bubble_sort(arr):
    n = len(arr)
    for i in range(n-1):
        for j in range(n - i - 1 ):
            if arr[j] > arr[j+1]:
                arr[j] , arr[j + 1 ] = arr[j + 1 ] , arr[j]


# Example usage
arr = [5, 3, 8, 4, 2]
bubble_sort(arr)
print("Sorted Array:", arr)


