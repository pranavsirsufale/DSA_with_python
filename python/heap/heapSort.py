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
        





