import matplotlib.pyplot as plt
import matplotlib as mpl
import pandas as pd
import numpy as np
import pylab as plt

df_train = pd.read_csv('https://www.rootsystems.pt/train.csv')
print(df_train.head())
print(df_train.tail())

print(df_train.dtypes)

print(df_train.describe())

print(df_train.isnull().any())
print()

print(df_train.info())

df_train2 = df_train.drop('Cabin', axis=1)
df_train.info()

media_idade = df_train2['Age'].mean()
mediana_idade = df_train2['Age'].median()
print(media_idade)
print(mediana_idade)

df_train2['Age'].hist()
plt.title('Idade')
plt.show()

df_train2['Age'].fillna(media_idade, inplace=True)
df_train2['Age'].hist()

media_idade = df_train2['Age'].mean()
mediana_idade = df_train['Age'].median()

print(media_idade)
print(mediana_idade)

df_train2['Age'].hist()
plt.title('Idade')
plt.show()

df_train2['Age'].fillna(media_idade, inplace=True)
df_train2['Age'].hist()
plt.title('Idade')
plt.show()

print(df_train2.groupby('Embarked')["PassengerId"].count())

df_train2['Embarked'].fillna('S', inplace=True)
print(df_train2.info())

df_train2.to_csv('train_no_nulls', index=False)