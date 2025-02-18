

'''
#? 1 ] Find the smallest element in the unsorted part.

#? 2 ] Swap it with the first unsorted element.

#? 3 ] Move the boundary between sorted and unsorted parts.
'''


def selection_sort(arr):
    for i in range(len(arr)):
        min_idx = i 
        for j in range(i+1 , len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i] , arr[min_idx] = arr[min_idx],arr[i]

# Example usage
arr = [29, 10, 14, 37, 13]
selection_sort(arr)
print(arr)