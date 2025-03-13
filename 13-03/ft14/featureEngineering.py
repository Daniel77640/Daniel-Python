import matplotlib.pyplot as plt
import matplotlib as mpl
import pandas as pd
import numpy as np
import pylab as plt

df_train = pd.read_csv('train_no_nulls_no_outliers.csv')
df_train.head(2)

novas_colunas = pd.get_dummies(df_train['Embarked'])
df_train2 = pd.concat([df_train,novas_colunas], axis=1)
print(df_train2.head(3))

df_train2.drop('Embarked', axis=1, inplace=True)
