

'''

### MERGE SORT
def merge_sort(arr):
    if len(arr) <= 1:
        return arr ###??? BAse case : already

    mid = len(arr) // 2
    left_half = merge_sort(arr[:mid])
    right_half = merge_sort(arr[mid:])
    return merge(left_half,right_half)


def merge(left , right):
    result = []
    i = j = 0

    ## Merge two sortted halves
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else :
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])

    return result

arr = [8, 3, 5, 4, 2, 7, 6, 1]
sorted_arr = merge_sort(arr)
print("Sorted Array:", sorted_arr)







### DFS
def dfs(graph,node,visited=None):
    if visited is None:
        visited = set()
    visited.add(node)
    print(node , end = ' ')

    for neighbor in graph[node]:
        if neighbor not in visited:
            dfs(graph,neighbor , visited)

    
graph = {
'A': ['B', 'C'],
'B': ['A', 'D', 'E'],
'C': ['A', 'F'],
'D': ['B'],
'E': ['B', 'F'],
'F': ['C', 'E']
}            

dfs(graph,'A')



#### Heap sort 
def heapify(arr,n,i):
    largest = i
    left = 2*i + 1
    right = 2*i + 2
    if left < n and arr[left]  > arr[largest]:
        largest = left
    if right < n and arr[right]> arr[largest]:
        largest = right
    if largest != i :
        arr[i],arr[largest] = arr[largest],arr[i]
        heapify(arr,i,0)

def heap_sort(arr):
    n = len(arr)
    for i in range(n //2 - 1 , -1 , -1):
        heapify(arr,n,i)
    for i in range(n-1,0,-1):
        arr[i],arr[0] = arr[0],arr[i]
        heapify(arr,i,0)

#example usage
arr = [12,11, 13, 5,6 ,6, 6, 66,53,3]
heap_sort(arr)
print(arr)
'''

### insertion sort 
def insertion_sort(arr):
    for i in range(1,len(arr)):
        key = arr[i]
        j = i -1
        while j >= 0 and key < arr[j]:
            arr[j + 1 ] = arr[j]
            j -= 1
        arr[j+1] = key

# Example usage
arr = [12, 11, 13, 5, 6]
insertion_sort(arr)
print(arr)      
















