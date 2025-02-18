
'''
###? 3] Recursively split the list into two halves until each half contains one element.

###? 2] Merge the halves in a sorted manner.
'''

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) //2 
        left = arr[:mid]
        right = arr[mid:]
        merge_sort(left)
        merge_sort(right)

        i = j = k  = 0 
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                
                i += 1 

            else : 
                arr[k] = right[j]
                j += 1 
            k += 1 
        
        while i < len(left):
            arr[k] = left[i]
            i += 1 
            k += 1 
        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1 

arr = [41,6,46,1,84,894,98,4,85,178,4,7941,8,4169]

merge_sort(arr)

print(arr)