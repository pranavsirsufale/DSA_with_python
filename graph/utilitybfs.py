import queue


def addEdge(adj,u,v):
    adj[u].append(v)

#? A utlity funciton tod o BFS of 
def BFSUtils(u,adj,visited):
    q = queue.Queue() 
    visited[u] = True
    q.put(u)

    while not q.empty():
        u = q.queue[0]
        print(u,end=' ')

        q.get() 





