# -*- coding: utf-8 -*-
"""
Created on Fri Jul 22 14:41:00 2022

@author: marko.ilioski
"""

import pandas as pd
import numpy as np 

#Sreduvanje so duplikati ama nema dplikati
Train = pd.read_csv('train.csv')
Train.drop_duplicates( inplace=True)

#Sreduvanje Outliers
Q1_Purchase = Train['Purchase'].quantile(0.25)
Q3_Purchase = Train['Purchase'].quantile(0.75)

IQR_Purchase = Q3_Purchase - Q1_Purchase
print (Q1_Purchase, Q3_Purchase, IQR_Purchase)

print (Train)

OutlierFilter = np.logical_or(Train['Purchase'] < (Q1_Purchase - 1.5 * IQR_Purchase),
                    Train['Purchase'] > (Q3_Purchase + 1.5 * IQR_Purchase))
Outliers = Train [OutlierFilter]
Train = Train [~OutlierFilter]
print(Train)


