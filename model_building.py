#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 24 12:08:07 2020

@author: iman
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('eda_data.csv')
#### To Do
# Choose relavant columns
# get dummy variables
# train test split
# multiple linear regression
# lasso regression
# random forest
# tune models GridSearchCV
# test ensembles

df_model = df[['avg_salary', 'rating', 'size', 'type of ownership', 'industry', 
               'sector', 'revenue', 'job_state', 'age', 'python', 'R', 'spark', 
               'aws', 'cloud', 'seniority', 'desc_len']]
# dummy variables
df_dum = pd.get_dummies(df_model)

# train test split
from sklearn.model_selection import train_test_split
X = df_dum.drop('avg_salary', axis=1)
y = df_dum['avg_salary'].values
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, 
                                                    random_state=42 )


# multiple linear regression
import statsmodels.api as sm
X = sm.add_constant(X)
model = sm.OLS(y, X)
print(model.fit().summary())

from sklearn.linear_model import LinearRegression
from sklearn.model_selection import cross_val_score

lm = LinearRegression()

print(np.mean(cross_val_score(lm, X_train, y_train, scoring='neg_mean_absolute_error', cv=3)))


# lasso regression
# random forest
# tune models GridSearchCV
# ensemble models
