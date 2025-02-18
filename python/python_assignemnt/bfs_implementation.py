
'''
##?? 1 ]o Start at the given node (root).

###?? 2]  Mark the node as visited and enqueue it.

###?? 3] While the queue is not empty, dequeue a node, print it, and enqueue its unvisited neighbors.
'''

from collections import deque

def bfs(graph,start):
    visited = []
    queue = deque([start])
    while queue:
        node = queue.popleft()
        if node not in visited:
            print(node , end = ' ')
            visited.append(node)
            for neighbor in graph[node]:
                queue.append(neighbor)

graph = {
'A': ['B', 'C'],
'B': ['A', 'D', 'E'],
'C': ['A', 'F'],
'D': ['B'],
'E': ['B', 'F'],
'F': ['C', 'E']
}

bfs(graph,'A')
