# The ky idea behind RAdix sort is to exploit the concept of place value 
# It assumes that sorting numbers digit by will eventaully result in a fully 
# sorted list.

# Least signifact digit (LSD) RAdix 


#! find the largest element in the array. and itelrate the times of digits 

#! sort the element based on the unit place digits (x=0). we use a stable sorting techniques,such as counting sort,to sort the digits at
#! eahc significant place. It's important to understand that the default implementation of counign sort is unstable 
#! to solve this problem we cna iterate the input array in reverse order to built the output array this srategy helps us to keep the same kesys in 

#? Code 
def counting_sort(arr,exp1):
    n = len(arr)
    # the output array element that will have sorted arr
    output = [0] * (n)
    # initializat count array as 
    count = [0] * (10)
    # store count of occurrences in count[]

    for i in range(0,n):
        index = arr[j] // exp1
        count[index % 10] += 1
        



counting_sort([546,4,68,4,98,4,5],804)



