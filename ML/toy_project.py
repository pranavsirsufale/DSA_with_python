import numpy as np
import pandas as pd

df = pd.read_csv('ML/placement-dataset.csv')

print(df.head())

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