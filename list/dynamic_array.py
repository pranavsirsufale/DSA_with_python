'''
import sys
L = []

# dynamic array expanding array size by 8 >>>
for i in range(100):
    sys.getsizeof(L)
    L.append(i)


'''




'''
ctypes is a foreign function library for Python. It provides
 C compatible data types, and allows calling functions in DLLs or 
 shared libraries. It can be used to wrap these libraries in pure 
 Python.
'''
# using c's array we are creaging python's list
import ctypes


class MeraList:
    def __init__(self):
        self.size = 1
        self.n = 0
        # create a C type array with size = self.sizse 
        self.A = self.__make_array(self.size)

    def __len__(self):
        return self.n
    
    def __str__(self):
        #[1,2,3]
        result = ''
        for i in range(self.n):
            result += str(self.A[i]) + ' , '
        return '[ ' + result[:-2] + ']'
    
    def __getitem__(self,index):
        if 0 <= index < self.n:
            return self.A[index]
        else : 
            return 'IndexError - Index out of range'

    




    def append(self,item):
        if self.n == self.size: # need to resize
            # resize 
            self.__resize(self.size *2 )
        # append
        self.A[self.n] = item
        self.n += 1


    def pop(self):
        if self.n == 0:
            return "Empty List"
        print(self.A[self.n-1])
        self.n -= 1

    
    
    
    


    def clear(self):
        self.n = 0
        self.size = 1


    def find(self,item):
        for i in range(self.n):
            if self.A[i] == item : 
                return i
        return 'ValueError - not in list'
    


    def __delitem__(self,index):
        if index >= self.n or index < 0 :
            return 'IndexError - not vlaid index'
        # delte from the position
        for i in range(index,self.n-1):
            self.A[i] = self.A[i+1]     
        self.n -= 1

    def insert(self,index,item):
        if self.size == self.n :
            self.__resize(self.size * 2)

        for i in range(self.n, index,-1):
            self.A[i] = self.A[i-1] 
        self.A[index] = item
        self.n += 1

    def remove(self,item):
        for i in range(self.n-1):
            if self.A[i] == item:
                self.__delitem__(i)
                return
        return "ValueError - item not found "

        




    def __resize(self,new_capacity):
        # create a new array with new capacity
        B = self.__make_array(new_capacity)
        self.size = new_capacity
        # copy the content of A to B
        for i in range(self.n):
            B[i] = self.A[i]
        # reassign A
        self.A = B

    def __make_array(self,capacity):
        # this code creates a C types (static,referential array) with size capacity
        return (capacity*ctypes.py_object)()

L = MeraList()
L.append('Pranav')
L.append(3.4)
L.append(True)
L.append(100)
L.append('infinite')
L.append('infinity')

print("length of L : " , len(L))

print(L)
# print(L[0])
# L.pop()
L.insert(2,'pooja')
# print(L.find('Pranav')) # found in position index 0
print(L)
print(L.__delitem__(500))
print(L)
print(L.remove('infinite'))
print(L.remove('infinite'))
print(L)



