
##?  1: stat at the given node (root)

##?  2: Mark the node as visited and enqueue it 

##?  3: While the queue is not empty, dequeue a node, print it. 


from collections import deque

def bfs(graph,start):
    visited = []

    queue = deque([start])

    while queue:
        node = queue.popleft()

        if node not in visited:
            print(node , end = ' ')
            visited.append(node)


