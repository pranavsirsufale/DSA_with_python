import heapq

def dijkstra(graph,start):
    pq = [] # Min-heap ( priority queue )
    distances = { node : float('inf') for node in graph}
    distances[start] = 0 
    heapq.heappush(pq, (0 , start))

    