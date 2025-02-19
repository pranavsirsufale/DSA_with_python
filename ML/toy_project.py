import numpy as np
import pandas as pd

df = pd.read_csv('ML/placement-dataset.csv')

print(df.head())

df = df.iloc[:,1:]
print('_____________MAXIMUM ------------------------------')
print(df.max())
print('------------------- MININUM  ------------------------------')
print(df.min())
print('----------------------- RANGE------------------------------')
print((df.max()) - (df.min()))
# print(df)
