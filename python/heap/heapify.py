# to heapify a subtree rooted to node which is 
# an index of arr[] adn dn is the size of heap 

def heapify(arr, n , i ):
    largest = i 
    l = 2*i + 1
    r = 2*i + 2 
    # if left child is largest than root 
    if ( l < n and arr[l] > arr[largest] ) : 
        largest = l 

    # if the right is larger 
    if ( r < n and arr[r] > arr[largest]) : 
        largest = r 

    # if root is not larger 
    if ( largest != i ):
        arr[i] , arr[largest] = arr[largest] , arr[i] 
        ### ! recursively heapify the affected subtree
        heapify(arr,n,largest)


#function to delte the root from heap 
def deleteRoot(arr):
    global n 
    ### Get the last element 
    lastElement = arr[n-1]

    ## Replace root with last element
    arr[0] = lastElement

    # decrease the size of heap by 1
    n -= 1
    heapify(arr, n , 0 )

def printArray(arr, n ):
    for i in range(n):
        print(arr[i], end = ' ')
    print()


if __name__ == '__main__':
    arr = [ 10,1,21,51,51,61,61,,651,651,65,416]

    n = len(arr)
    deleteRoot(arr)
    printArray(arr,n)



