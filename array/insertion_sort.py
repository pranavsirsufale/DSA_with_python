'''
algo
1 ) we start with second element of the array as fist
elemn in the array is assumed to be sorted.

2) Compare second element with th efirst eleme and check
if the second element is smaller than swap them

3) move to the third element and compare it wit the 
second element, then the first element and swap as necessary to put it in the 
correct position among the first there elements.


4) continue this process, computing each element with the ones befroe it and swapping
as needed to place it in the correct
position among th esorted elem 

5) Repeat until the entire array is sorted




'''
import mailbox

def insertion_sort(arr):
    # 1 ) we start with second element of the array as fist elemn in the array is assumed to be sorted.
    for i in range(1,len(arr)):
        key = arr[i]
        j = i-1
        #2) Compare second element with th efirst eleme and check if the second element is smaller than swap them
        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            j-= 1
        arr[j+1] = key
# Auxiliary function to print array of size n 
def print_array(arr):
    for i in range(len(arr)):
        print(arr[i],end=" ")
    print()
    print(arr)

if __name__ == "__main__":
    arr = [12,11,13,5,6]
    insertion_sort(arr)
    print_array(arr)
  