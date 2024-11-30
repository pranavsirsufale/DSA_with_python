from collections import deque

def bfs(adj,start):
    queue = deque()
    visited = [False] * len(adj)
    visited[start] = True
    queue.append(s)
    while queque:
        #dequeue a vertex from queue and print it
        curr = q.popleft()
        print(curr,end=" ")
        # get all adjscent vertices of the dequeue
        #vertext it an ajjacesnt has been visited
        # mark it visited and queue
        for x in adj[curr]:
            if not visited[x]:
                visited[x] = True
                queue.append(x)

 # Function to add on edge to the graph
def add_edge(adj,u,v):
    adj[u].append(v)
    adj[v].append(u)  
    

    # Example usage
if __name__ == "__main__":
    # Number of vertices in the graph
    v = 5
    # Adjucency list representation of the graph
    adj = [ for _ in range(v)]
    add_edge(adj,0,1)
    add_edge(adj,0,2)
    add_edge(adj,1,3)
    add_edge(adj,1,4)
    add_edge(adj,2,4)
    print(adj)

    # perform BFS traversal stratgy from vertext 0
    print('BFS starting from 0 : ')
    bfs(adj,0)   
        
