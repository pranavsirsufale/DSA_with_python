'''
-> first increase the heap size by 1 . so that it cna store the new element

-> insert the new element at the end of the heap 

-> This newly inserted element may distort the properties of heap for its paretn's . so in order to keep the 
   properties of heap . heapify this newly inserted element following a bottom up approach

'''

###? Bottom - up approach 
def heapify(arr,n , i ): 
    parent  = int( ((i - 1 ) / 2 ))

    ###? For max heap if current node is greater than its parent , swap both of them and call heapify again for the parent 
    if parent >= 0 : 
        if arr[i] > arr[parent]:
            arr[i],arr[parent] = arr[parent] , arr[i]

            # Recursively heapify the paretnode 
            heapify(arr,n,parent)


def insertNode(arr, key):
    global n 
    
    # Increase the size of heap by 1 

    n += 1
    # insert the element at end of heap 
    arr.append(key)

    # Heapify the new node following a Bottom up approach 
    heapify(arr, n , n -1 )