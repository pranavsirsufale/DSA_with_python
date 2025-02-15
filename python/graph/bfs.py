from collections import deque
# BFS from given source s 
def bfs(adj,s,visited):
    q = deque() ####??? create a queue for BFS
    ####!!! Mark the source node as visited and enqueue it 
    visited[s] = True
    q.append(s)
    while q:
        curr = q.popleft() ####! Dequeue a vertext 
        print(curr, end = ' ')

        ###!! Get all adjacent vertext of curr 
        for i in adj[curr]:
            if not visited[i]:
                visited[i] = True ###?? Mark visited 
                q.append(i) ####? Enqueue it 


####??? Function to add an edge to the graph 
def add_edge(adj,u,v):
    adj[u].append(v)
    adj[v].append(u) ### Undirected graph


###? Perform BFS for the entire graph
def bfs_disconnected(adj):
    visited = [False] * len(adj) ####! not visited 

    for i in range(len(adj)):
        if not visited[i]:
            bfs(adj,i,visited)


### Example usage
v = 6 
adj = [[] for _ in range(v)]

# add ege to the graph 
add_edge(adj,0,1)
add_edge(adj,0,2)
add_edge(adj,3,4)
add_edge(adj,4,5)

bfs_disconnected(adj)