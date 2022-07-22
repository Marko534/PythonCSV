# -*- coding: utf-8 -*-
"""
Created on Fri Jul 22 14:41:00 2022

@author: marko.ilioski
"""

import pandas as pd
import numpy as np 

Train = pd.read_csv('train.csv')
Train = Train.drop_duplicates()
Columns = Train.columns
for i in Columns:
    print (Train[i].value_counts(), '\n')
# print (Train.duplicated())
# Train = Train.drop_duplicates()
# print (Train.duplicated())
