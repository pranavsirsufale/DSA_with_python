####??? Undirected graph 
class Graph:
    def __init__(self,vertices):
        # Adjacency list
        self.adj == [[] for _ in range(vertices)]

    def addEdge(self,s,t):
        self.adj[s].append(t)
        self.adj[t].append(s)

    def dfs_rec(self,visited,s):
        visited[s] = True
        print(s,end = " ")


        ##3 Recursively visit all adjacency vertex
        # that are not visited yet
        for i in self.adj[s]:
            if not visited[i]:
                self.dfs_rec(visited,i)
    
    def dfs(self):
        visited = [False] * len(self.adj)
        #### Loop through all verteces to handle disconnected graph 
        for i in range(len(self.adj)):
            if not visited[i]:
                ####??? perform DFS from unvisited vertext
                self.dfs_rec(visited,i)










