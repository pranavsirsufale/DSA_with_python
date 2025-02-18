
'''
###?? 1]Build a max heap.

###?? 2]Swap the root (largest element) with the last element.

###?? 3]Reduce the heap size and heapify the tree again.

###?? 4]Repeat until the heap size is reduced to 1.
'''

def heapify(arr,n,i):
    largest = i 
    left = 2*i +1 
    right = 2*i +2 
    if left < n and arr[left] > arr[largest]:
        largest = left

    if right < n and arr[right] > arr[largest]:
        largest = right 
    
    if largest != i:
        arr[i] , arr[largest] = arr[largest] , arr[i]
        heapify(arr,n,largest)
