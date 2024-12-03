import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import pandas as pd
import plotly.express as px
import squarify
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


x = [i for i in range(1,11)]
y = [8,7,6,4,5,6,7,8,9,10]

plt.xticks(np.arange(11))
plt.yticks(np.arange(11))

plt.scatter(x,y,s=500,c='g')

plt.title('scatter plot',fontsize=25)
plt.xlabel('x-axis',fontsize=18)
plt.ylabel('y-axis',fontsize = 18)

plt.show()



from matplotlib import style
data = np.random.random(50)
print(data)
print(plt.style.available)

plt.style.use('Solarize_Light2')
# plt.style.use('seaborn-v0_8-whitegrid')
plt.plot(data)
plt.show()



data = {'x': [1, 2, 3, 4], 'y': [10, 20, 15, 25]}
print(data)
sns.scatterplot(x='x', y='y', data=data)
plt.title("Scatter Plot")
plt.show()


import seaborn as sns
import matplotlib.pyplot as plt

data = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
sns.heatmap(data, annot=True, cmap='coolwarm')
plt.title("Heatmap")
plt.show()



dates = pd.date_range('2023-01-01',end='2023-12-30',periods=10)
values = [5,6,7,8,7,6,5,4,3,2]
plt.plot(dates,values,marker='o')
plt.title('Time Series Plot example')
plt.xticks(rotation=45)

print(len(dates))

plt.show()



dates = pd.date_range(start='2020-01-01',end='2020-12-31',freq="D")

print(len(dates))

data = np.random.random(len(dates))

df = pd.DataFrame(data,index=dates,columns=['Value'])

plt.figure(figsize=(10,6))

plt.plot(df.index,df['Value'],label='Trend')


plt.xlabel('date')
plt.ylabel('Values')

plt.grid(True)

plt.legend()

plt.show()








data = np.random.random(5)
sns.heatmap(data,cmap='coolwarm',annot=True,fmt='2f')

plt.title('heatmap with cowarm')

plt.show()
data = np.array([[85,75,65,90],
                [78,82,88,70],
                [92,80,87,85],
                [65,60,70,75],
                [95,88,85,92]])
xlable = ['math','science','english','history']
ylable = ['student','student 2','student 3','4','5']

plt.figure(figsize=(8,6))
sns.heatmap(data,annot=True,cmap='Greens',xticklabels=xlable,yticklabels=ylable,fmt='d')


plt.title("students grade across subjects ",fontsize=16)
plt.xlabel('subjects',fontsize=12)
plt.ylabel('Sutudents',fontsize=12)

plt.savefig('plot.png')

plt.show()



sizes = [20,15,10,5]
labes = ['a','b','c','d']
squarify.plot(sizes=sizes,label=labes,alpha=1.0)

plt.title('Treemap example')
plt.show()



size = [500,300,200,100,50]
label = ['Electronics','clothing','glroceries','furniture','toys']
colors = ['#ffaaac','#66b3ff','#aaffaa','#abccba','#ffccaa']
plt.figure(figsize=(8,6))

squarify.plot(sizes=size, label=label,color=colors, alpha=0.8)

plt.title('sales distribution by category')

plt.axis('off') # to off the axis

plt.show()




market_share = [40,25,15,10,5,5]
lables = ['company','company b','company c','comapny d','company e','company f']
colors = ['red','green','blue','yellow','purple','white']

# plt.figure(figsize=(10,7))
squarify.plot(sizes=market_share,label=lables,color=colors,alpha=0.7)

plt.title('market share by company')

plt.show()



population = [4436,1215,738,423,42,38]

labels = ['Asia','Africa','Europe','North a','South A','rasia']

colors = ['green','red','blue','purple','yellow','orange']

plt.figure(figsize=(10,8))

squarify.plot(sizes=population,label=labels,color=colors,alpha=0.8)
plt.title('world population by continetns')
plt.axis('on')

plt.show()






budget = [50,35,25,20,15,10]

colors = ['red','green','blue','yellow','purple','white']

labeles = ['R&D' , 'Marketing','HR','sales','IT','Operation']

labels_with_value = [f'{label} \n  ${bud}' for label, bud in zip(labeles, budget)]

plt.figure(figsize=(10,7))

squarify.plot(sizes=budget,label=labels_with_value,color=colors,alpha=0.8)

plt.show()








regions = ['north','south','east','west']
product_a_sales = [40,50,60,70]

product_b_sales = [30,40,50,60]

product_c_sales = [20,30,40,50]

figwidth= 0.5

index = np.array(len(regions))

ax.bar(index,product_a_sales,figwidth)




categories = ['cat1','2','3']

values1 = [5,7,3]
values2 = [4,6,8]
value3 = [2,5,7]

x = np.arange(len(categories))

plt.bar(x,values1,label='Group A',color='skyblue')
plt.bar(x,values2,bottom=values1,label='Group b',color='salmon')
plt.bar(x,value3,bottom=np.array(values1) + np.array(values2),label='Gropup C',color='lightgreen')

plt.xticks(x,categories)
plt.legend()

plt.show()




categories = ['Category A', 'Category B', 'Category C', 'Category D']
values = [25, 35, 20, 20]

plt.pie(values,labels=categories,autopct='%1.1f%%',startangle=90)

plt.title('BAsic pie chart')

plt.show()






'''

# Data
categories = ['Category A', 'Category B', 'Category C', 'Category D']
values = [25, 35, 20, 20]
colors = ['gold', 'lightblue', 'lightcoral', 'lightgreen']

explode = [0.2,0,0,0]

plt.pie(values,labels=categories,autopct='%1.1f%%',startangle=140,colors=colors,explode=explode,shadow=True)

plt.show()



# data = np.random.random(10,10)