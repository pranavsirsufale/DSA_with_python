# Initialization enqueue the graph source vertex

from collections import deque
# BFS from given source s 
def bfs(adj,s,visited ):
    q = deque() # create queue for BFS
    # Mark the source node as visited and enqueue it



    visited[s] = True
    q.append(s)
    while q:
        curr = q.popleft() # Dequeu a vertex
        print(curr,end=' ')

        # Get all adjacent vertices of curr

        for x in adj[curr] :
            if not visited[x]:
                visited[x] = True  # mark as visited 
                q.append(x)


def add_edge(adj,u,v):
    adj[u].append(v)
    adj[v].append(v)


## perform BFS for the entire graph

def bfs_disconnected(adj):
    visited = [False] * len(adj)


    
    for i in range(len(adj)):
        if not visited[i]:
            bfs(adj, i,visited)


# example usage 
v=6
adj= [[] for _ in range(v)]  # adjancancy list


print(adj)


'''

0 --- 1 --

'''


# add edge to the graph
add_edge(adj,0,1)
add_edge(adj,0,2)
add_edge(adj,3,4)
add_edge(adj,4,5)


bfs_disconnected(adj)







def bubble_sort(arr):
    n = len (arr)
    for i in range(n -1):
        for s in range(n -1):
            if arr[s] > arr[s + 1]:
                arr[s], arr[s + 1] = arr[s+1], arr[s]
                return arr

            #Example usages

            numbers = [66,88,77,45,64,99,45]
            sorted_number = bubble_sort(numbers)
            Print("sorted arry:", sorted_number)
def bubble_sort(arr):
  
    # Outer loop to iterate through the list n times
    for n in range(len(arr) - 1, 0, -1):
        
        # Initialize swapped to track if any swaps occur
        swapped = False  

        # Inner loop to compare adjacent elements
        for i in range(n):
            if arr[i] > arr[i + 1]:
              
                # Swap elements if they are in the wrong order
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                
                # Mark that a swap has occurred
                swapped = True
        
        # If no swaps occurred, the list is already sorted
        if not swapped:
            break


# Sample list to be sorted
arr = [39, 12, 18, 85, 72, 10, 2, 18]
print("Unsorted list is:")
print(arr)

bubble_sort(arr)

print("Sorted list is:")
print(arr)

