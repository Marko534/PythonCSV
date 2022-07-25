# -*- coding: utf-8 -*-
"""
Created on Fri Jul 22 14:41:00 2022

@author: marko.ilioski
"""
import pandas as pd
import numpy as np

#Sreduvanje so duplikati ama nema dplikati
Train = pd.read_csv('train.csv')
Train.drop_duplicates(inplace=True)

#Detecting the Missing Values and filling them
TrainWithoutNull = Train

for i in Train['Product_Category_1']:
    TrainWithoutNull = Train['Product_Category_2'].loc[Train['Product_Category_1'] == i].fillna(value =  Train['Product_Category_2'].loc[Train['Product_Category_1'] == i].mean())

print (Train)
print (TrainWithoutNull)
#Sreduvanje Outliers
Q1_Purchase = Train['Purchase'].quantile(0.25)
Q3_Purchase = Train['Purchase'].quantile(0.75)

IQR_Purchase = Q3_Purchase - Q1_Purchase

OutlierFilter = np.logical_or(Train['Purchase'] < (Q1_Purchase - 1.5 * IQR_Purchase),
                              Train['Purchase'] > (Q3_Purchase + 1.5 * IQR_Purchase))
Outliers = Train[OutlierFilter]
TrainWithoutOutliers = TrainWithoutNull[~OutlierFilter]


#Histogram
# Train['Purchase'].hist()
# TrainWithoutNull['Purchase'].hist()
# TrainWithoutOutliers['Purchase'].hist()

#BoxPlot

# Train.boxplot( by = 'Gender', column = ['Purchase'])
# TrainWithoutNull.boxplot( by = 'Gender', column = ['Purchase'])
# TrainWithoutOutliers.boxplot( by = 'Gender', column = ['Purchase'])

