##Node class
class Node:
    def __init__(self,data):
        self.data = data 
        self.next = None

# Linked list class
class LinkedList:
    def __init__(self):
        self.head = None

    ### Insert at the end 
    def append(self,data):
        new_node = Node(data)
        if not self.head :
            self.head = new_node
            return
        last = self.head
        while last.next : 
            last = last.next
        last.next = new_node


    ### Insert at the beginning
    def prepend(self,data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    # Delete a node 
    def delete(self,key):
        temp = self.head

        # If the node to be deleted is the head
        if temp and temp.data == key:
            self.head = temp.next
            temp = None 
            return
        prev = None 
        while temp and temp.data != key:
            prev = temp
            temp = temp.next

        if temp is None:
            return 
        
        prev.next = temp.next
        temp = None

    def print_list(self):
        temp = self.head
        while temp : 
            print(temp.data, end = ' -> ')
            temp = temp.next
        print("None")

ll = LinkedList()
ll.print_list()  # Output: 0 -> 1 -> 2 -> 3 -> None
ll.append(1)
ll.append(2)
ll.append(3)
ll.print_list()  # Output: 0 -> 1 -> 2 -> 3 -> None
ll.prepend(0)
ll.print_list()  # Output: 0 -> 1 -> 2 -> 3 -> None

ll.delete(2)
ll.print_list()  # Output: 0 -> 1 -> 3 -> None
