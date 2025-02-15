## python code to implement fibonnacci series
# function for fibonaccie
def fib(n):
    print(n)
    # stop condition 
    if(n == 0 ):
        return 0
    # stop condition
    if ( n== 1 or n == 2 ):
        return 1
    # recursive function
    else : 
        return ( fib(n-1 ) + fib(n-2))

# driver code
if __name__ == "__main__":
    # initial variable
    n = 5 
    print('fibonaccie series of number is : ', end = " ")

    # for loop to print the fibonaccie series 
    for i in range(0,n):
        print(fib(i),end=' ')