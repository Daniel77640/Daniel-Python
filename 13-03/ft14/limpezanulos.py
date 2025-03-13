import matplotlib.pyplot as plt
import matplotlib as mpl
import pandas as pd
import numpy as np
import pylab as plt

df_train = pd.read_csv('https://www.rootsystems.pt/train.csv')
print(df_train.head())
print(df_train.tail())

print(df_train.dtypes)