def print_star(n):
    start = 1
    for i in range(n,-1, -1):
        print((i * ' ' ) + ( start*'*'))
        start += 2
till = 5
print(print_star(till))


