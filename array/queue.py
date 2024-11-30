from collections import deque

queue = deque()

queue.append('element')
queue.append('text')
queue.append('element 3')

def del_item(q,item):
    for i in range(len(q)-1):
        if q[i] == item:
            del q[i]

want_to_delete = 'text'

del_item(queue,want_to_delete)


print(queue)
