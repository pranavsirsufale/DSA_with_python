import heapq

def dijkstra(graph,start):
    pq = [] # Min-heap ( priority queue )
    distances = { node : float('inf') for node in graph}
    distances[start] = 0 
    heapq.heappush(pq, (0 , start))

    while pq:
        current_distance , current_node = heapq.heappop(pq)

        if current_distance > distances[current_node]:
            continue

        for neighbor, weight in graph[current_node]:
            distance = current_distance + weight


            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(pq,(distance,neighbor))

    return distances


# example graph ( Adjacency List )
graph = {
    "A":[("B",4), ("C",1)],
    "B":[('C',2)],
    "C":[]
}

print(dijkstra(graph,'A'))