from collections import deque
# Bfs from given source s 
def bfs(adj,s,visited):
    q = deque() 

    visited[s] = True
    q.append(s)
    while q:
        curr = q.popleft() 
        print(curr, end = ' ')

        for x in adj[curr]:
            if not visited[x]:
                visited[x] = True
                q.append(x) 

            
def addEdge(adj,u,v):
    adj[u].append(v)
    adj[v].append(u)


# Perform BFS for the entire graph 
def bfs_disconnected(adj):
    visited = [False] * len(adj)

    for i in range(len(adj)):
        if not visited[i]:
            bfs(adj,i,visited)


v = 6
adj = [[] for _ in range(v)]

##? add ege to the graph 
addEdge(adj,0,1)
addEdge(adj,0,2)
addEdge(adj,3,4)
addEdge(adj,4,5)

bfs_disconnected(adj)