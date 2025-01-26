from collections import deque
#! BFS from given source s 
def bfs(adj,s,visited):
    print(s)
    q = deque()
    #? Mark the source node as visited and enqueue it 
    visited[s] = True 
    q.append(s)
    while q:
        curr = q.popleft()  # dequeue a vertext
        print(curr)
        print(curr,end=' ')
        # Get all adjacent verteces of curr 
        for x in adj[curr]:
            if not visited[x]:
                visited[x] = True  #? Mark visited 
                q.append(x) # Enqueu it 

#! Function to add and edge to the graph 
def add_edge(adj,u,v):
    print('EDGE U AND V :::::', u, v )
    adj[u].append(v)
    adj[v].append(u) #? Undirected graph

#! Perform BFS for the entire graph
def bfs_disconnected(adj):
    visited = [False] * len(adj)  #? No visited 
    for i in range(len(adj)):
        if not visited[i]:
            bfs(adj,i,visited)

#! Example usage 
v = 6 
adj = [[] for _ in range(v)] # adjacancy list

# add edge to the graph 
add_edge(adj,0,1)
add_edge(adj,0,2)
add_edge(adj,3,4)
add_edge(adj,4,5)
bfs_disconnected(adj)