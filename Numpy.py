import numpy as np
import pandas as pd
data = [15, 16, 18, 19, 22, 24, 29, 30, 34]
print("MEAN",np.mean(data))
print("MEDIAN",np.median(data))
print("50",np.mean(data))
print("MEAN",np.mean(data))
print("MEAN",np.mean(data))
df = pd.read_csv('https://sololearn.com/uploads/files/titanic.csv')
print(df.head())
print("-----------")
pd.options.display.max_columns = 6
col = df['Fare']
print(df.describe())
print(col)
print("-----------")
small_df =df[['Age', 'Sex', 'Survived']]
print(small_df.head())
print("-----------")
df['male'] = df['Sex'] =='male'
print(df.head())
print("-----------")
print(df['Fare'].values.shape)