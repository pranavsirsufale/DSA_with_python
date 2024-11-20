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
