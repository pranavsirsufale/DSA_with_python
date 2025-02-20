
'''
###?? 1 ] Start at the given node (root).

###?? 2] Mark it as visited.

###?? 3] Recursively visit all unvisited neighbors.
'''
def dfs(graph,node,visited=None):
    if visited == None:
        visited = set()
    visited.add(node)
    print(node, end = ' ')
    for neighbor in graph[node]:
        if neighbor not in visited:
            dfs(graph,neighbor,visited)

graph = {
'A': ['B', 'C'],
'B': ['A', 'D', 'E'],
'C': ['A', 'F'],
'D': ['B'],
'E': ['B', 'F'],
'F': ['C', 'E']
}

dfs(graph,'A')





