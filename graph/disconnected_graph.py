import queue
#? A utility function to add an edge 
#? in an undirected graph

def addEdge(adj,u,v):
    adj[u].append(v)
# A utitlity function to do BFS of 
#! graph from a given vertext u.

def BFSutils(u,adj,visited):
    # create a queue for BFS 
    q = queue.Queue()
    #! Mark the current node as visisted and enqueue it
    visited[u] = True 
    q.put(u)

    #! 'i' will be used to get all adjancnacy vertex 4 of a vertext list<int>
    while (not q.empty()):
        #! Dequeue a vertex from queue and print it 
        u = q.queue[0]
        print(u,end=' ')
        q.get()
        #! GET ALL ADJACANCY VERTICES OF THE DEQUE VERTEX S . IF AN ADJACENT HAS NOT BEEN VISITED, THEN MARK IT VISITED
        #! THEN MARK IT VISITED AND ENQUEU IT 
        i = 0 
        while i != len(adj[u]):
            if(not visited[adj[u][i]]):
                visited[adj[u][i]] = True
                q.put(adj[u][i])
            i += 1 

#! THIS FUNCTION DOES BFS UTILS () FOR ALL UNVISITED VERTICES.

def BFS(adj,v):
    visited = [False] * v
    for u in range(v):
        if ( visited[u] == False ) : 
            BFSutils(u,adj,visited)


#? DRIVER CODE 
if __name__ == '__main__':
    v = 5 
    adj = [[] for i in range(v)]
    addEdge(adj,0,4)
    addEdge(adj,1,2)
    addEdge(adj,1,3)
    addEdge(adj,1,4)
    addEdge(adj,2,3)
    addEdge(adj,3,4)
    BFS(adj,v)