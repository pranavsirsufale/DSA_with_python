'''
IN CASE OF DISCONNECTED GRAPH OF ANY VERTEX THAT IS UNREACHABLE FROM ALL VERTEX, THE PREVIOUS 
EXAMPLE WILL NOT GIVE OUTPUT 

JUST TO MODIFY BFS PERFORM SIMPLE BFS FROM EACH UNVISITED VERTEXT OF GIVEN GRAPH 

'''
import queue
# A utility function to add an edge
# in an undirected graph 
def addEdge(adj,u,v):
    adj[u].append(v)


#?? A utility function to do BFS of 
#?? grpah from a given vertext u
def BFSUtils(u,adj,visited):
    q = queue.Queue()

    ### Mark the current node as visited 
    # and enqueue it 
    visited[u] = True
    q.put(u)

    ### i will be used to get all adjacent vertextes 4 of a vertext us 
    while ( not q.empty() ):
        ####? Dequeue a vertext from queue and print it
        u = q.queue[0]
        print(u,end = ' ')
        u = q.get()

        ### Get all adjacency verteces of the 
        # deque vrtext s if an adjacent # has not been visited then mark it visited and enque it 
        i = 0 
        while i != len(adj[u]):
            if ( not visited[adj[u][i]]):
                visited[adj[u][i]] = True
                q.put(adj[u][i])
            i += 1 

# This funciton does BFS utils () for all unvisited vertex

def bfs(adj,v):
    visited = [False] * v
    for u in range(v):
        if ( visited[u] ==  False) :
            BFSUtils(u,adj,visited)


### Driver code 
if __name__ == '__main__':
    print(__name__)
    v = 5 
    adj = [[] for _ in range(v)]
    addEdge(adj,0,4)
    addEdge(adj,1,2)
    addEdge(adj,1,3)
    addEdge(adj,1,4)
    addEdge(adj,2,3)
    addEdge(adj,3,4)













    ###########################################

    import queue
# A utility function to add an edge
# in an undirected graph 
def addEdge(adj,u,v):
    adj[u].append(v)


#?? A utility function to do BFS of 
#?? grpah from a given vertext u
def BFSUtils(u,adj,visited):
    q = queue.Queue()

    ### Mark the current node as visited 
    # and enqueue it 
    visited[u] = True
    q.put(u)

    ### i will be used to get all adjacent vertextes 4 of a vertext us 
    while ( not q.empty() ):
        ####? Dequeue a vertext from queue and print it
        u = q.queue[0]
        print(u,end = ' ')
        u = q.get()

        ### Get all adjacency verteces of the 
        # deque vrtext s if an adjacent # has not been visited then mark it visited and enque it 
        i = 0 
        while i != len(adj[u]):
            if ( not visited[adj[u][i]]):
                visited[adj[u][i]] = True
                q.put(adj[u][i])
            i += 1 

# This funciton does BFS utils () for all unvisited vertex

def bfs(adj,v):
    visited = [False] * v
    for u in range(v):
        if ( visited[u] ==  False) :
            BFSUtils(u,adj,visited)


### Driver code 
if __name__ == '__main__':
    print(__name__)
    v = 5 
    adj = [[] for _ in range(v)]
    addEdge(adj,0,4)
    addEdge(adj,1,2)
    addEdge(adj,1,3)
    addEdge(adj,1,4)
    addEdge(adj,2,3)
    addEdge(adj,3,4)