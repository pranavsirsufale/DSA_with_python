# python to heapify a subtree rooted with nodes 
# which is an index in arr []

def heapify(arr,n,i):
    #? Initialize largest as root
    largest = i 
    l = 2*i + 1 
    r = 2*i + 2 

    ##?? If left child is largest thna parent 
    if ( l < n and arr[l] > arr[largest] ):
        largest = l 

    if ( r < n and arr[r] > arr[largest] ):
        largest = r

    ###? If the root is not largest
    if largest != i :
        arr[i] , arr[largest] = arr[largest] , arr[i]

        ##!!!! Recursively heapify the 

        heapify(arr,n,largest)


# main function to do heap sort
def heapSort(arr):
    n = len(arr)

    # Build heap ( rearrange array )
    for i in range(n // 2 -1 , -1 , -1):
        heapify(arr,n,i)

    # one by one extracdt an element from heap 
    for i in range(n-1 , 0 , -1):
        ### Move root to end 
        arr[0],arr[i] = arr[i],arr[0] 

        ### Call max heapfify on the reduced heap 
        heapify(arr,i,0) 



        
def printArray(arr):
    print(end='| ')
    for i in arr:
        print(i, end = ' | ')
    print()

arr = [9,4,3,8,1,464,64,1,496,165,418,96,641,984,6525,5641,2,848,5]
heapSort(arr)
print('sorted array is ')
printArray(arr) 




