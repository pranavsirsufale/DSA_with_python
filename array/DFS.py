graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G'],
    'D': [],
    'E': [],
    'F': [],
    'G': []
}



def dfs_iterative(graph,start):
    visited = set()
    stack = [start]

    while stack:
        node = stack.pop()  # Remove the top of the stack
        if node not in visited:
            print(node,end=' ')     # Process the node
            visited.add(node)
            # Add neighors in reverse order to maintain order
            stack.extend(reversed(graph[node]))


# Driver code
print('\nDFS (Iterative) : ', end=" ")
dfs_iterative(graph,'A')



def dfs_recursive(graph,node,visited):
    if node not in visited:
        print(node,end=" ") # process the node
        visited.add(node)   # Mark as visited
        for neighbor in graph[node]:
            dfs_recursive(graph,neighbor, visited)


# Driver code
visited = set()
print('DFS (REcurive):' , end=" ")
dfs_recursive(graph,'A',visited)




import networkx as nx

# Create the graph
G = nx.Graph()
G.add_edges_from([('A', 'B'), ('A', 'C'), ('B', 'D'), ('B', 'E'), ('C', 'F'), ('C', 'G')])



# Perform DFS
dfs_nodes = list(nx.dfs_preorder_nodes(G, source='A'))
print("\nDFS using NetworkX:", dfs_nodes)
