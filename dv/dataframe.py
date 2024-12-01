'''
import matplotlib.pyplot as plt
import pandas as pd
data = [['pranav',99],['pooja',100],['pillu',400]]
df = pd.DataFrame(data,columns=['Name','Mark'])
print(df)
stud_name = ['ram','pranav','pooja','pillu','pallavi']
stud_mark = [20,98,99,100,100]
plt.plot(stud_name,stud_mark)
plt.xlabel("Student Name")
plt.ylabel('Student Mark')
plt.title("Student Makrs")
# plt.show()
'''

import matplotlib.pyplot as plt
x = [1,2,3,4,5,6,7,8,9,10]
y = [10,20,30,40,50,60,70,80,90,100]
plt.scatter(x,y)
plt.xlabel('x-axis')
plt.ylabel('y-label')
plt.title('scatter graph')







