class Graph:
    def __init__(self,vertices):
        self.adj = [[] for _ in range(vertices)]

    def addEdge(self,s,t):
        self.adj[s].append(t)
        self.adj[t].append(s)

    def dfs_rec(self,visited,s):
        visited[s] = True
        print(s,end=' ')

        for i in self.adj[s]:
            if not visited[i]:
                self.dfs_rec(visited,i)
    
    def dfs(self):
        visited = [False] * len(self.adj)
        for i in range(len(self.adj)):
            if not visited[i]:
                self.dfs_rec(visited,i)

    
if __name__ == '__main__':
    v = 6 
    graph = Graph(v)
    # Define edge of the graph 
    edges = [(1,2),(2,0),(0,3),(4,5)]

    for edge in edges:
        graph.addEdge(edge[0],edge[1])

    print("Complete DFS of the grpah ")
    graph.dfs()