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
Product_Category_1 = TrainWithoutNull['Product_Category_1'].unique()

for i in Product_Category_1:
    Product_Category_1Mean = TrainWithoutNull['Product_Category_2'].loc[TrainWithoutNull['Product_Category_1'] == i].mean()
    TrainWithoutNull['Product_Category_2'].loc[TrainWithoutNull['Product_Category_1'] == i] = TrainWithoutNull['Product_Category_2'].loc[TrainWithoutNull['Product_Category_1'] == i].fillna(value = Product_Category_1Mean)

TrainWithoutNull['Product_Category_2'] = TrainWithoutNull['Product_Category_2'].round(0)
TrainWithoutNull['Product_Category_2'] = TrainWithoutNull['Product_Category_2'].fillna(value = 0)

Product_Category_2 = TrainWithoutNull['Product_Category_2'].unique()
print (Product_Category_2)


for i in Product_Category_1:
    for j in Product_Category_2:
        Product_Category_2Mean = TrainWithoutNull['Product_Category_3'].loc[(TrainWithoutNull['Product_Category_1'] == i) & (TrainWithoutNull['Product_Category_2'] == j)].mean()
        TrainWithoutNull['Product_Category_3'].loc[(TrainWithoutNull['Product_Category_1'] == i) & (TrainWithoutNull['Product_Category_2'] == j)] = TrainWithoutNull['Product_Category_3'].loc[(TrainWithoutNull['Product_Category_1'] == i) & (TrainWithoutNull['Product_Category_2'] == j)].fillna(value = Product_Category_2Mean)

TrainWithoutNull['Product_Category_3'] = TrainWithoutNull['Product_Category_3'].round(0)
TrainWithoutNull['Product_Category_3'] = TrainWithoutNull['Product_Category_3'].fillna(value = 0)

#Sreduvanje Outliers
Q1_Purchase = TrainWithoutNull['Purchase'].quantile(0.25)
Q3_Purchase = TrainWithoutNull['Purchase'].quantile(0.75)

IQR_Purchase = Q3_Purchase - Q1_Purchase

OutlierFilter = np.logical_or(TrainWithoutNull['Purchase'] < (Q1_Purchase - 1.5 * IQR_Purchase),
                              TrainWithoutNull['Purchase'] > (Q3_Purchase + 1.5 * IQR_Purchase))
Outliers = TrainWithoutNull[OutlierFilter]
TrainWithoutOutliers = TrainWithoutNull[~OutlierFilter]


#Histogram
Train['Purchase'].hist()
TrainWithoutNull['Purchase'].hist()
TrainWithoutOutliers['Purchase'].hist()

#BoxPlot

Train.boxplot( by = 'Gender', column = ['Purchase'])
TrainWithoutNull.boxplot( by = 'Gender', column = ['Purchase'])
TrainWithoutOutliers.boxplot( by = 'Gender', column = ['Purchase'])

