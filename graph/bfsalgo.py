from collections import deque
# BFS from given source s
def bfs(adj,s,visited):
    q = deque()
    visited[s] = True
    q.append(s)
    while q : 
        curr = q.popleft() 
        print(curr, end = ' ')
        for x in adj[curr]:
            if not visited[x]:
                visited[x] = True
                q.append(x)

# Function to add an edge to the graph
def add_edge(adj,u,v):
    adj[u].append(v)
    adj[v].append(u)


# perform BFS for the entire graph
def bfs_disconnected(adj):
    visited = [False] * len(adj)
    for i in range(len(adj)):
        if not visited[i]:
            bfs(adj,i,visited)

v = 6 
adj = [[] for _ in range(v)]

add_edge(adj,0,1)
add_edge(adj,0,2)
add_edge(adj,3,4)
add_edge(adj,4,5)

print(adj)

bfs_disconnected(adj)