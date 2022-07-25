# -*- coding: utf-8 -*-
"""
Created on Thu Jul 21 12:15:24 2022

@author: marko.ilioski
"""

import pandas as pd
import numpy as np 

Train = pd.read_csv('train.csv')

TrainWithoutNull = Train

for i in Train['Product_Category_1']:
    TrainWithoutNull = Train['Product_Category_2'].loc[Train['Product_Category_1'] == i].fillna(value =  Train['Product_Category_2'].loc[Train['Product_Category_1'] == i].mean())

print (Train)
print (TrainWithoutNull)


# print (Train[['Product_Category_1', 'Product_Category_2']])
# print (Train[['Product_Category_1', 'Product_Category_2']].loc[Train['Product_Category_1'] == 1])

print (Train.tail())

x = Train.describe(include = 'all')
print (x)

print (Train.info())