#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun  2 10:07:21 2018

@author: sparsh
"""

import pandas as pd
import numpy as np
data = pd.read_csv('ex1data1.txt',names=['Population','Profit'])

data.head()

data.describe()
data.plot(kind='scatter',x = 'Population',y='Profit',figsize=(4,3))

def computeCost(X, y, theta):  
    inner = np.power(((X * theta.T) - y), 2)
    return np.sum(inner) / (2 * len(X))

data.insert(0, 'Ones', 1)
data

cols = data.shape[1]  
cols
X = data.iloc[:,0:cols-1]  
y = data.iloc[:,cols-1:cols]
X.values

x1 = np.matrix(X.values)
y1 = np.matrix(y.values)
theta = np.matrix(np.array([0,0])) 

sum = computeCost(x1,y1,theta)
