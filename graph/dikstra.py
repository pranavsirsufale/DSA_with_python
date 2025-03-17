import heapq

def dijkstra(graph,start):
    pq = [] # min-heap (priority queue)
    distances = {node : float('inf') for node in graph }
    distances[start] = 0 
    heapq.heappush(pq , ( 0 , start))

    while pq:
        current_distance, current_node = heapq.heappop(pq)

        if current_distance > distances[current_node]:
            continue

        for neibhbor, weight in graph[current_node]:
            distances = current_distance + weight 

            if distances < distances[neibhbor]:
                distances[neibhbor] = distances 
                heapq.heappush(pq,(distances, neibhbor))

    return distances

# Example Graph ( Adjacency List )
graph = {
    'A' : [('B',4), ('C',1)],
    'B':[('C',2)],
    "C":[]
}

print(dijkstra(graph,'A'))
