####??? Undirected graph 
class Graph:
    def __init__(self,vertices):
        # Adjacency list
        self.adj = [[] for _ in range(vertices)]

    def addEdge(self,s,d):
        self.adj[s].append(d)
        self.adj[d].append(s)

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

if __name__ == "__main__":
    v = 6 ###?? Number of vertext
    graph = Graph(v)

    # Define the edge of the graph 
    edges = [(1,2), (2,0), (0,3), (4,5)]

    ### Populate the adjacency lis twith edge
    for edge in edges:
        graph.addEdge(edge[0], edge[1])

    print('complete DFS of the graph ')
    graph.dfs()


    '''
                        APPROACH

1. THE IDEA IS TO DO DFS OF A GIVEN GRAPH 

2 > 1 > 3 
2 > 0 > 3 
2 > 0 > 1 > 3 

2. START THE DFS TRAVERSAL FROM THE SOURCE 

3. KEEP STORING THE VISITED VERTECES IN AN ARRAY OR HASHMAP SAY 'path[]'

4. iF THE DESTINATION VERTEXT IS REACHED. PRINT THE CONTENTS OF PATH[]

5. THE IMPORTANT THING IS TO MARK CURRENT VERTICES IN THE PATH [] AS VISITED ALSO SO THAT THE 
TRAVERSAL DOESN'T GO IN A CYCLE 


    '''

