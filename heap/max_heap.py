import heapq

def priority_queue(pq):
    # create a copy of the priority queue to avoid modifying the original 
    q = pq[:]
    # Extract elements form the max-heap and print them in descending order
    while q:
        print(-heapq.heappop(q),end=' ')
    print()

def main():
    # Initialize an empty priority queue (min-heap for negatives to simulate a max-heap)
    q = []
    # Push elements into the heap (negated for max-heap simulation)
    heapq.heappush(q, -10)
    heapq.heappush(q, 3)  # -(-3) is 3, hence using positive
    heapq.heappush(q, -7)
    heapq.heappush(q, -8)
    
    # Show the priority queue contents
    priority_queue(q)

if __name__ == "__main__":
    main()
