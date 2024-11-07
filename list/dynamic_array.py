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
        self.n -= 1




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
L.append('Pooja maz pillu')
L.append(3.4)
L.append(True)
L.append(100)

print("length of L : " , len(L))

print(L)
print(L[0])



