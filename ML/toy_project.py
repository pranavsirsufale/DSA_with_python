import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

df = pd.read_csv('ML/placement-dataset.csv')

# print(df.info())

# print(df.head())

df = df.iloc[:,1:]
# print('_____________MAXIMUM ------------------------------')
# print(df.max())
# print('------------------- MININUM  ------------------------------')
# print(df.min())
# print('----------------------- RANGE------------------------------')
# print((df.max()) - (df.min()))
# print(df)


## STEPS 
###? 0.  PREPROCESSING - EDA + FEATURE SELECTION
###? 1 . eXTRACT INPUT AND OUT COLS
###? 2. SCALE THE VALUES
###? 3. TRAIN TEST SPLIT
###? 4. TRAIN THE MODEL
###? 5. EVALUATE THE MODEL/MODEL SELECTION
###? 6 . DEPLOY THE MODEL 




plt.scatter(df['cgpa'],df['iq'],c=df['placement'])
# plt.show()

### classify using linear regression

### Indipendent variables
X = df.iloc[:,0:2]

# dependent variable
y = df.iloc[:,-1]

####?? Scale the values 

############ ( independent , dependent , size )
X_train , X_test , y_train, y_test = train_test_split(X, y, test_size= 0.1, )

scaler = StandardScaler() 

X_train = scaler.fit_transform(X_train)

X_test = scaler.transform(X_test)
clf = LogisticRegression() 

#### Model training
fitt = clf.fit(X_train,y_train)

# print(fitt)
y_pred = clf.predict(X_test)

print(y_pred)

score = accuracy_score(y_test,y_pred)

print(score)

from mlxtend.plotting import plot_decision_regions

plot_decision_regions(X_train, y_train.values, clf = clf, legend=2)
