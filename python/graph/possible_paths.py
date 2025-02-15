####!  all paths from source to target

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


###!!! PYTHON PROGRAM TO PRINT ALL PATHS FROM A SOURCE TO DESTITIONA
from collections import defaultdict

#### This class represents a directed graph 
# using adjacency list representation 
class Graph:
    def __init__(self,vertices):
        ### No. of vertices 
        self.v = vertices 

        # Default dictionary to store graph 
        self.graph = defaultdict(list)

    #### function to add an edge to graph 
    def addEdge(self,u,v):
        self.graph[u].append(u)


    '''
    A RECURSIVE FUNCTION TO PRINT AL PATHS FROM U TO AD  . VISITED[] KEEPS TRACK OF VERTICES IN CURRENT PATH 
    PATH[] STORES ACTUAL VERTICES AND PATH_INDEX IS CURRENT INDEX IN PATH[]
    '''
    def printAllPathsUtils(self,u,d,visited,path):
        # mark the current node as visited and store in path 
        visited[u] = True
        path.append(u)

        ### If current vertext is same as destination then print
        ### Current path[]

        if u == d:
            print(path)
        else:
            ### If currrent vertix isnot destination 
            ### recur for all the vertices adjacent to this vertex
            for i in self.graph[u]:
                if visited[i] == False:
                    self.printAllPathsUtils(i,d,visited,path)

        #### REmove current vertex from path[] and mark it as unvisited 

        path.pop()
        visited[u] = False

    ### print s all paths from s to d 
    def printAllpaths(self,s,d):
        # mark all the vertices as not visited
        visited = [False] * (self.v)

        ### createa an array to stor epth
        path = []

        # call the recursive helper function to ptint all paths 
        self.printAllPathsUtils(s,d,visited,path)

### create a graph given in the above diagram 
g = Graph(4)
g.addEdge(0,1)
g.addEdge(0,2)
g.addEdge(0,3)
g.addEdge(2,0)
g.addEdge(2,1)
g.addEdge(1,3)
s = 2; d = 3 
g.printAllpaths(s,d)