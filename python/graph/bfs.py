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