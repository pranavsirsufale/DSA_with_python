# recursively dividing the input array into smaller subarrys and sorting those subarrays and them mmergin them back together to 
# obtain the sorted array




def merge_sort(arr):
    if(len(arr) <= 1):
        return arr
    mid = len(arr) // 2
    print(mid)

    left_half = arr[:mid]
    print('LEFT ARRAY : ',left_half)


    right_half = arr[mid:]
    print('RIGHT ARRAY : ',right_half)

    sorted_left = merge_sort(left_half)

    sorted_right = merge_sort(right_half)

    return merge(sorted_left,sorted_right)

def merge(left,right):
    result = []
    i = j = 0
    while i < len(left) and j< len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else : 
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    
    result.extend(right[j:])
    return result

unsorted_array = [3,7,6,-10,15,23,5,55,-13]
sorted_array = merge_sort(unsorted_array)

print(sorted_array)

    