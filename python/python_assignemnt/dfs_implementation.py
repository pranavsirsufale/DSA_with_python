
#??? 1> Start at the given node ( root )

#??? 2 > Mark it as visited 

#??? 3 > Recursively visit all unvisited neighbors.


def dfs(graph,node,visited = None) : 
    if visited is None:
        visited = []

    visited.append(node)

    print(node, end = ' ')
    for neighbor in graph[node]:
        if neighbor not in visited:
            dfs(graph,neighbor,visited):





