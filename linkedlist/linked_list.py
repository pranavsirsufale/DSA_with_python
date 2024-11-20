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


    def delete_head(self):
        if self.head == None:
            #empty 
            return 'Empty lInked list'
        self.head = self.head.next
        self.n = self.n -1



    def pop(self):

        if self.head == None:
            # empty 
            return 'Empty LL'


        # kya linked list me 1 item hai
        if curr.next == None : 
            # head hi hoga ( delete from head)
            return 
        curr = self.head
        while curr.next.next != None:
            curr = curr.next
        
        # curr -> 2nd last node
        curr.next = None
        self.n = self.n -1

    
    def remove(self,value):
        if self.haed == None:
            return 'Empty linked list'

        if self.head.data == value:
            # you want to remove the head node
            return self.delete_head()


        curr = self.head

        while curr.next != None:
            if curr.next.data == value:
                break
            curr = curr.next
        # 2 cases item mil gaya
        # item nai mila 

        if curr.next == None:
            # item nahi mila
            return "Not found"
        else:
            curr.next = curr.next.next

    def search(self,item):
        curr = self.head
        pos = 0

        while curr != None:
            if curr.data == item:
                return pos
            curr = curr.next
            pos = pos + 1
        return 'Not Found'

    def __getitem__(self,index):
        curr = self.head
        pos = 0

        while curr != None:
            if pos == index:
                return curr.data
            curr = curr.data
            pos += 1
        return "indexError"


    





        





L = LinkedList()

L.insert_head(4)
L.insert_head(3)
L.insert_head(2)
L.insert_head(1)
L.append(5)
L.append("pranav ")
print(len(L))

print(L)


'''
Given a linked list of characters, write a python function to return a new string that is creaated by 
# appending all the characters given in the linekd list as per the rules given below 


# rules >
# replace '*' or '/' by a single space
# In case of two constructive occurences of '*' '/'. replace those two occurences by a single space and 
convert the next chacater to upper case

# assume that ->
there will not be more than two consecutive occurences of '*' or '/'
# The linked list will always end with an alphabet


# sample input
# An Apple a day Keeps A Doctor way

expected output



'''














