def selection_sort(arr):
    n = len(arr)
    for i in range(n-1):
        # assume the current position holds the minimum elem
        min_idx = i
        # Iterate through the unsorted portion
        # To find the actual minimum 
        for j in range(i+1,n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        # a new minimum is found swap it with th eelem at index 
        if min_idx != i:
            arr[i],arr[min_idx]=arr[min_idx],arr[i]

def print_array(arr):
    for val in arr:
        print(val,end=" ")
    # print()

if __name__ == "__main__" : 
    arr = [51,6,8,98,4,98,4198,49,8,4,65,1,564]
    selection_sort(arr)
    print_array(arr)