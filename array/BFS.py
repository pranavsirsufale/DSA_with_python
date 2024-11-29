def bfs(graph,start):
    visited = set()   # set keep track of visited notes
    queue = []      # que to take reference

    queue.append(start)
    visited.add(start)


    while queue:
        node = queue.pop(0)
        print(node)

        # Explore neighbors
        for neighbor in grap[node]:
            if neighbor not in visited:
                queue.append(neighbor)
                visited.add(neighbor)
