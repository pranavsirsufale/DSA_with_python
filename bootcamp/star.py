def print_star(n):
    start = 1
    for i in range(n,-1, -1):
        print((i * ' ' ) + ( start*'*'))
        start += 2
till = 5
print(print_star(till))


def alagram(text1,text2):
    if len(text1) != len(text2):
        return 'strings are not having same length'
    if sorted(text1) != sorted(text2):
        return 'not sharing same characters '
    else:
        return f" The both strings '{text1}' and '{text2}' are sharing the same characters"
    
tex1 = 'something'
tex2 = 'thingsome'

print(alagram(tex1,tex2))