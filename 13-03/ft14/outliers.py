import matplotlib.pyplot as plt
import matplotlib as mpl
import pandas as pd
import numpy as np
import pylab as plt

df_train = pd.read_csv('train_no_nulls.csv')
print(df_train.describe())
print(df_train.sort_values('Age', ascending=False).head(5)['Age'])
print(df_train.sort_values('Age', ascending=True).head(5)['Age'])

media_idade = df_train['Age'].mean()
df_train.loc[df_train['Age'] ==133, 'Age'] = media_idade
print(df_train.sort_values('Fare', ascending=False).head(5)['Fare'])
print(df_train.sort_values('Fare', ascending=True).head(5)['Fare'])

mediana_tarifa = df_train['Fare'].median()
df_train.loc[df_train['Fare']>5000, 'Fare'] = mediana_tarifa
df_train.loc[df_train['Fare']<0, 'Fare'] = mediana_tarifa
print(df_train.sort_values('Fare', ascending=False).head(5)['Fare'])
print(df_train.sort_values('Fare', ascending=True).head(5)['Fare'])

df_train.to_csv('train_no_nulls_no_outliers.csv', index=False)
