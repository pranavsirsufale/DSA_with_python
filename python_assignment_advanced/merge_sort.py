'''
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2 
        left = arr[:mid]
        right = arr[mid:]

        print('LEFT ARRAY', left)
        print('RIGHT ARRAY', right)

        merge_sort(left)
        merge_sort(right)

        i = j = k = 0 
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
arr = [38, 27, 43, 3, 9, 82, 10]
merge_sort(arr)
print(arr)        

def merge_sort(arr):
    if len(arr) <= 1 : 
        return arr ###??? Base Case : Already sorted
    
    mid = len(arr) // 2 
    left_half = merge_sort(arr[:mid]) ###?? recursively sort left half
    right_half = merge_sort(arr[mid:]) ###?? Recursively sort right half

    return merge(left_half, right_half)

def merge(left,right):
    result = []
    i = j = 0 

    # Merge two sorted halves 
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1 
        else:
            result.append(right[j])
            j += 1
    ## ADd any remainging elelments
    result.extend(left[i:])
    result.extend(right[j:])



    return result

arr = [8, 3, 5, 4, 2, 7, 6, 1]
sorted_arr = merge_sort(arr)
print("Sorted Array:", sorted_arr)
'''

def merge_sort(arr):
    if len(arr) <= 1:
        return arr ##?? Base case : already sorted

    mid = len(arr) //2
    left_half = merge_sort(arr[:mid])
    right_half = merge_sort(arr[mid:])

    return merge(left_half,right_half)

def merge(left,right):
    result = []
    i = j = 0 

    # Merge two sortted halves 
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else : 
            result.append(right[j])
            j += 1
    # add any remainnig elements
    result.extend(left[i:])
    result.extend(right[j:])
    
    return result

arr = [8, 3, 5, 4, 2, 7, 6, 1]
sorted_arr = merge_sort(arr)
print("Sorted Array:", sorted_arr)