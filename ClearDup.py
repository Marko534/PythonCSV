# -*- coding: utf-8 -*-
"""
Created on Fri Jul 22 14:41:00 2022

@author: marko.ilioski
"""
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

#Sreduvanje so duplikati ama nema dplikati
Train = pd.read_csv('train.csv')
Train.drop_duplicates(inplace=True)

#Detecting the Missing Values and filling them
TrainWithoutNull = Train
Product_Category_1 = TrainWithoutNull['Product_Category_1'].unique()

for i in Product_Category_1:
    Product_Category_1Mean = TrainWithoutNull['Product_Category_2'].loc[TrainWithoutNull['Product_Category_1'] == i].mean(
    )
    TrainWithoutNull['Product_Category_2'].loc[TrainWithoutNull['Product_Category_1'] ==
                                               i] = TrainWithoutNull['Product_Category_2'].loc[TrainWithoutNull['Product_Category_1'] == i].fillna(value=Product_Category_1Mean)

TrainWithoutNull['Product_Category_2'] = TrainWithoutNull['Product_Category_2'].round(
    0)
TrainWithoutNull['Product_Category_2'] = TrainWithoutNull['Product_Category_2'].fillna(
    value=0)

Product_Category_2 = TrainWithoutNull['Product_Category_2'].unique()


for i in Product_Category_1:
    for j in Product_Category_2:
        Product_Category_2Mean = TrainWithoutNull['Product_Category_3'].loc[(
            TrainWithoutNull['Product_Category_1'] == i) & (TrainWithoutNull['Product_Category_2'] == j)].mean()
        TrainWithoutNull['Product_Category_3'].loc[(TrainWithoutNull['Product_Category_1'] == i) & (TrainWithoutNull['Product_Category_2'] == j)] = TrainWithoutNull['Product_Category_3'].loc[(
            TrainWithoutNull['Product_Category_1'] == i) & (TrainWithoutNull['Product_Category_2'] == j)].fillna(value=Product_Category_2Mean)

TrainWithoutNull['Product_Category_3'] = TrainWithoutNull['Product_Category_3'].round(
    0)
TrainWithoutNull['Product_Category_3'] = TrainWithoutNull['Product_Category_3'].fillna(
    value=0)

#Sreduvanje Outliers
Q1_Purchase = TrainWithoutNull['Purchase'].quantile(0.25)
Q3_Purchase = TrainWithoutNull['Purchase'].quantile(0.75)

IQR_Purchase = Q3_Purchase - Q1_Purchase

OutlierFilter = np.logical_or(TrainWithoutNull['Purchase'] < (Q1_Purchase - 1.5 * IQR_Purchase),
                              TrainWithoutNull['Purchase'] > (Q3_Purchase + 1.5 * IQR_Purchase))
Outliers = TrainWithoutNull[OutlierFilter]
TrainWithoutOutliers = TrainWithoutNull[~OutlierFilter]


#Histogram
def histogram ():
    Bins = range(0, 21400, 1000)
    plt.hist(TrainWithoutOutliers['Purchase'], bins = Bins, color = '#3495eb')
    plt.xticks(Bins[::3])
    plt.title("Histogram")
    plt.xlabel('Amount spent')
    plt.ylabel('Number of people')
    plt.show()

def boxPlotGender():
    print (TrainWithoutOutliers['Gender'].loc[TrainWithoutOutliers['Gender'] == 'M'])
    plt.boxplot([
        TrainWithoutOutliers['Purchase'].loc[TrainWithoutOutliers['Gender'] == 'M'],
        TrainWithoutOutliers['Purchase'].loc[TrainWithoutOutliers['Gender'] == 'F']],
        labels=(['Male', 'Female']))
    plt.xlabel('Sex')
    plt.ylabel('Total Spent')
    plt.show()
    
boxPlotGender()