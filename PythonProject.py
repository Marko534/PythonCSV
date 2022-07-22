# -*- coding: utf-8 -*-
"""
Created on Thu Jul 21 12:15:24 2022

@author: marko.ilioski
"""

import pandas as pd

Traint = pd.read_csv('train.csv', index_col='User_ID')

print (Traint.head())
print (Traint.tail())