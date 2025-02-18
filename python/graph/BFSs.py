from collections import deque
def bfs(adj,s,visited):
    q = deque() 
    visited[s] = True
    q.append(s)
    while q:
        curr = q.popleft() #### Dequeue a vertex 
        print(curr , end = ' ')
        for x in adj[curr]:
            if not visited[x]:
                visited[x] = True
                q.append(x) 

def add_edge(adj,u,v):
    adj[u].append(v)
    adj[v].append(u)

def bfs_disconnected(adj):
    visited = [False] * len(adj)





