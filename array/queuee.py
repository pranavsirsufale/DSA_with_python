from collections import deque
# Create a queue
queue = deque()

#Enqueue operation (add elements)
queue.append("A")
queue.append('B')
queue.append('C')
queue.append('C')

print('Queue after enqueue : ',queue)

# Dequeue operatino ( rmeove elements )
elements = queue.popleft()
print('Dequeue element : ' , elements)
print('Dequeu elements : ',elements)
print("Queue after dequeue",queue)






