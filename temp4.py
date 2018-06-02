#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun  2 11:11:56 2018

@author: sparsh
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
data = pd.read_csv('ex1data1.txt',delimiter=',',names=['Population','Profit'])

X = data.iloc[:,:1].values;
Y = data.iloc[:,1:2].values;


from sklearn.cross_validation import train_test_split
X_train,X_test,Y_train,Y_test = train_test_split(X,y,test_size = 1/3)


from sklearn.linear_model import LinearRegression

reg = LinearRegression()
reg.fit(X_train,Y_train)

y_pred = reg.predict(X_test)
y_pred

plt.scatter(X_train,Y_train,color="red")
plt.plot(X_train,reg.predict(X_train),color="blue")

plt.scatter(X_test,Y_test,color="red")
plt.plot(X_test,y_pred,color="blue")
