# -*- coding: utf-8 -*-
"""
Created on Thu Jul 21 12:15:24 2022

@author: marko.ilioski
"""

import pandas as pd
import numpy as np 

Train = pd.read_csv('train.csv')

print (Train.head())
print (Train.tail())

x = Train.describe(include = 'all')
print (x)

print (Train.info())