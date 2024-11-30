



def selection_sort(arr):
    n = len(arr)
    print(n)
    boundry = 0
    small = 0
    while boundry != n+1:
        print(boundry)
        
        for i in range(boundry,n):
            if arr[small] > arr[i]:
                small = i
    print(arr[small])
                
            

arr = [165,6541,651,64864,15,164165,16,1,5146165,65,15,6]
selection_sort(arr)
