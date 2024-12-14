
lis = []

for n in range(100,920):
    # print ("number ")
    flag = True 
    for i in range(2,n):
        if n %i == 0 :
            flag = False
            break
    
    if flag:
        lis.append(n)

print(lis)