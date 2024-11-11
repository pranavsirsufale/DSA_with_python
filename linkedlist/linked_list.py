class Node:
    def __init__(self,value):
        self.data = value 
        self.next = None


"""
a = Node(1)
b = Node(2)
c = Node(3)

a.next = b
b.next = c
print('B node connected to the node  : ',(id(b.next)))
print(id(a))
print(id(b))
print(id(c))

"""


class LinkedList:
    def __init__(self):
        self.head = None     # create empty linked list
        self.n = 0  # number of nodes In the LL

    def __len__(self):
        return self.n
    
    def insert_head(self,value):
        # new node
        new_node = Node(value)

        # create connection
        new_node.next = self.head 

        # reassign head
        self.head = new_node

        # increment 
        self.n += 1

    def __str__(self):
        curr = self.head
        result = ''
        while curr != None:
            result += str(curr.data) + ' -> '
            curr = curr.next
        return result[:-3]

    def append(self,value):
        new_node = Node(value)
        if self.n == None:
            self.head = new_node
            self.n += 1
            return
        

        curr = self.head
        while curr.next != None:
            curr = curr.next 

        # you are at the last node 
        curr.next = new_node
        self.n += 1


    def insert_after(self,after,value):
        new_node = Node(value)

        curr = self.head 

        while curr != None :
            if curr.data == after:
                break
            curr = curr.next
        # case 1 break -> item apko mil gaya -> curr -> not none
        if curr != None:
            # logic 
            new_node.next - curr.next
            curr.next = new_node
        else :
            return 'Item not found'


    def clear(self):
        self.head = None
        self.n = 0


    





        





L = LinkedList()

L.insert_head(4)
L.insert_head(3)
L.insert_head(2)
L.insert_head(1)
L.append(5)
L.append("pranav ")
print(len(L))

print(L)






