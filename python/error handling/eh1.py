file = open('my.txt','w')

try:
    file.write('pranav learning python')
finally:
    file.close()
with open('my.txt','w') as file:
    file.write('pranav teaching python')