from collections import deque

def bfs(graph,start):
    visited = set()         # To track visited nodes
    queue = deque([start])    # Initial a queue with the start
    visited.add(start)      # Mark the start node as visisted

    while queue:
        node = queue.popleft()  # Dequeue a node from the fton
        print(node,end=" ")     # Proess the node ( e.g, print)


        # Iterate through the neigbhors of the current node
        for neighbor in graph[node]:
            if neighbor not in visited:
                queue.append(neighbor) # Enqueue unvisited neighours
                visited.add(neighbor)   # Mark them as visited


# Example grpah represented as an adjecency list
graph = {
    'A':['B','C'],
    'B': ['A','D','E'],
    'C' : ['A','F'],
    'D': ['B'],
    'E' : ['B'],
    'F':['C']
}

# Run BFS starting from node 'A"
print('BFS Traversal : ')

bfs(graph,'A')



