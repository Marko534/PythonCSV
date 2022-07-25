# -*- coding: utf-8 -*-
"""
Created on Thu Jul 21 12:15:24 2022

@author: marko.ilioski
"""

import pandas as pd
import numpy as np 

Train = pd.read_csv('train.csv')

Product_Category_1 = Train['Product_Category_1'].unique()

for i in Product_Category_1:
    Product_Category_1Mean = Train['Product_Category_2'].loc[Train['Product_Category_1'] == i].mean()
    Train['Product_Category_2'].loc[Train['Product_Category_1'] == i] = Train['Product_Category_2'].loc[Train['Product_Category_1'] == i].fillna(value = Product_Category_1Mean)

Train['Product_Category_2'] = Train['Product_Category_2'].round(0)
Train['Product_Category_2'] = Train['Product_Category_2'].fillna(value = 0)

Product_Category_2 = Train['Product_Category_2'].unique()
print (Product_Category_2)


for i in Product_Category_1:
    for j in Product_Category_2:
        Product_Category_2Mean = Train['Product_Category_3'].loc[(Train['Product_Category_1'] == i) & (Train['Product_Category_2'] == j)].mean()
        Train['Product_Category_3'].loc[(Train['Product_Category_1'] == i) & (Train['Product_Category_2'] == j)] = Train['Product_Category_3'].loc[(Train['Product_Category_1'] == i) & (Train['Product_Category_2'] == j)].fillna(value = Product_Category_2Mean)

Train['Product_Category_3'] = Train['Product_Category_3'].round(0)
Train['Product_Category_3'] = Train['Product_Category_3'].fillna(value = 0)







print (Train.head())
print (Train.tail())

x = Train.describe(include = 'all')
print (x)

print (Train.info())