import matplotlib.pyplot as plt
import numpy as np
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

import matplotlib.pyplot as plt
import numpy as np
x = [1,2,3,4,5,6,7,8,9,10]
y = [10,20,30,40,50,60,70,80,90,100]
plt.scatter(x,y)
plt.xlabel('x-axis')
plt.ylabel('y-label')
plt.title('scatter graph')
plt.show()





import matplotlib.pyplot as plt
stud_name = ['ram','sham','rahul','rajesh','sahil']
stud_mark = [55,66,58,32,65]

plt.plot(stud_name,stud_mark)
plt.xlabel('Student Name')
plt.ylabel("Student marks ")
plt.title('Line Graph')
plt.show()






x = [1,2,3,4,5,6,7,8,9,10]
y= [10,20,30,40,50,60,70,80,90,100]
plt.scatter(x,y)
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.title('Scatter graph')
plt.show()
# scatter plot



x = np.array([5,7,8,7,2,7,2,9,4,11,12,9,6])
y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])
plt.xlabel("X - asxi")
plt.ylabel('Y- lables')
plt.scatter(x,y)
plt.show()





x = np.array([5,7,8,7,2,7,2,9,4,11,12,9,6])
y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])
plt.scatter(x,y)

x = np.array([9,4,11,12,9,65,7,8,7,2,7,2,8])
y = np.array([86,103,87,94,78,77,85,86,99,86,87,88,111])

plt.xlabel('X - axis')
plt.ylabel('y - axis')


plt.scatter(x,y)
plt.show()



xpoints = np.array([0,6])
ypoints = np.array([0,250])
plt.plot(xpoints,ypoints)
plt.show()




ypoints = np.array([3,8,1,10])
plt.plot(ypoints,marker='o')
plt.show()



ypoint = np.array([3,8,1,10])
plt.plot(ypoint,'o:r')
plt.show()



ypoint = np.array([3,8,1,10])
plt.plot(ypoint,linestyle='dotted')
plt.show()


y = [2,3,4.5]
y2 = [1,1.5,5]
plt.plot(y)
plt.plot(y2)
plt.legend(['blue','green'],loc='upper left')
plt.show()




y = [2,3,4.5]
y2 = [1,1.5,5]
plt.plot(y)
plt.plot(y2)

plt.legend(['blue','green'],loc='upper left')
plt.show()


y = [ x for x in range(1,1000)]

# print(y)
y2 = []
for i in y:
    y2.append(i**2)
# print(y2)

plt.plot(y,y,label='Numbers')
plt.plot(y,y2, label='Square of numbers')
plt.legend()
plt.show()



x_values = [i for i in range(1,6)]
y_values = [2,3,5,7,11]

buttle_size = [30,80,150,200,300]

plt.scatter(x_values,y_values,s=buttle_size,alpha=0.6,edgecolors='g',linewidths=2)
plt.title('Bubble chart with Trnsperancy')
plt.xlabel('x-axis')
plt.ylabel('y-label')
plt.show()


x = [1,2,3,4,5]
y1 = [2,4,6,8,10]
y2 = [3,6,9,12,15]


plt.scatter(x,y1)
plt.scatter(x,y2)
plt.legend(['x*2','x*3'])
plt.show()



x = [0.1,0.2,0.3,0.4,0.5]
y = [6.2,-8.4,8.5,9.2,-6.3]
size = [100,220,330,440,550]


plt.title('connected scatter plot points with lsense')
plt.scatter(x,y,s=size,alpha=0.6,edgecolors='b')
plt.plot(x,y)
plt.show()

'''



