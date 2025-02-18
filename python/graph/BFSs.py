from collections import deque
# BFS from given source s 
def bfs(adj,s,visited):
     
    q = deque() 

    visited[s] = True

    q.append(s)

    while q:
        curr = q.popleft() #### Dequeue a vertex 
        print(curr , end = ' ')
        
        # get all adjacent verteces of curr 

        for x in adj[curr]:
            if not visited[x]:
                visited[x] = True
                q.append(x) 


### function to add an edge to the graph
def add_edge(adj,u,v):
    adj[u].append(v)
    adj[v].append(u)









