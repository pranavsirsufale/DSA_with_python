class Node:
    def __init__(self,value):
        self.data = value
        self.next = None

class Linedlist:
    def __init__(self):
        #Empty linked list
        self.head = None
        # no of nodes in the ll
        self.n = 0

    def __len__(self):
        return self.n
    

    # ******
    def insert_head(self,value):
        # new node 
        new_node = Node(value)
        # Create connection
        new_node.next = self.head
        # reassign head
        self.head = new_node
        #increment 
        self.n += 1

    def __str__(self):
        curr = self.head
        result = ''
        while curr != None:
            result = result + str(curr.data) + '->'
            curr = curr.next
        return result[:-2]
    

l = Linedlist()
print(l.insert_head(10))
print(l.insert_head(20))
print(l.insert_head(30))
print(l.head)
