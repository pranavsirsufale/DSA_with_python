import queue

# A utility function to add an edge in an undirected graph 
def addEdge(adj, u, v):
    adj[u].append(v)
    adj[v].append(u)  # Ensure the graph is undirected

# A utility function to do BFS of graph from a given vertex u
def BFSUtils(u, adj, visited):
    q = queue.Queue()

    # Mark the current node as visited and enqueue it 
    visited[u] = True
    q.put(u)

    # Loop until queue is empty
    while not q.empty():
        # Dequeue a vertex from queue and print it
        u = q.get()
        print(u, end=' ')

        # Get all adjacent vertices of the dequeued vertex u
        # If an adjacent has not been visited, mark it visited and enqueue it
        for i in range(len(adj[u])):
            if not visited[adj[u][i]]:
                visited[adj[u][i]] = True
                q.put(adj[u][i])

# This function calls BFSUtils() for all unvisited vertices
def bfs(adj, v):
    visited = [False] * v
    for u in range(v):
        if not visited[u]:
            BFSUtils(u, adj, visited)

# Driver code 
if __name__ == '__main__':
    v = 5  # Number of vertices
    adj = [[] for _ in range(v)]
    
    addEdge(adj, 0, 4)
    addEdge(adj, 1, 2)
    addEdge(adj, 1, 3)
    addEdge(adj, 1, 4)
    addEdge(adj, 2, 3)
    addEdge(adj, 3, 4)

    print("BFS Traversal:")
    bfs(adj, v)
