def selection_sort(arr):
    n = len(arr)
    for i in range(n-1):
        min_idx = i
        for j in range(i+1,n):
            if arr[j] < arr[min_idx]:
                min_idx = j

                
        if min_idx != i:
            arr[i],arr[min_idx] = arr[min_idx],arr[i]
def print_array(arry):
    for val in arr:
        print(val,end=" ")
    print()


if __name__ == "__main__":
    arr =[46,646,61,641,614,61,6841,89,61864,684,69486,8654]
    print_array(arr)
    print(selection_sort(arr))
