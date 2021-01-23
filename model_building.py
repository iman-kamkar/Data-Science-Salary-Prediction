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
               'sector', 'revenue', 'hourly', 'employer_provided', 'job_state', 
               'age', 'python_yn', 'spark', 'aws', 'excel', 'seniority', 'desc_len', 
               'num_comp', 'same_state', 'job_title']]
# dummy variables
df_dum = pd.get_dummies(df_model)

# train test split
from sklearn.model_selection import train_test_split
X = df_dum.drop('avg_salary', axis=1)
y = df_dum['avg_salary'].values
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)


# multiple linear regression
import statsmodels.api as sm
X = sm.add_constant(X)
model = sm.OLS(y, X)
print(model.fit().summary())

from sklearn.linear_model import LinearRegression, Lasso
from sklearn.model_selection import cross_val_score

lm = LinearRegression()

print(np.mean(cross_val_score(lm, X_train, y_train, scoring='neg_mean_absolute_error', cv=3)))


# lasso regression
alpha = []
error = []

for i in range(1, 100):
    alpha.append(i/100)
    lasso = Lasso(alpha=i/100)
    error.append(np.mean(cross_val_score(lasso, X_train, y_train, scoring='neg_mean_absolute_error', cv=3)))

plt.plot(alpha, error)

err = tuple(zip(alpha, error))
err_df = pd.DataFrame(err, columns={'alpha', 'error'})
err_df[err_df.error == max(err_df.error)]
# random forest
from sklearn.ensemble import RandomForestRegressor

rf = RandomForestRegressor()

np.mean(cross_val_score(rf, X_train, y_train, 
                        scoring='neg_mean_absolute_error', cv=3))

# tune models GridSearchCV
from sklearn.model_selection import GridSearchCV, RandomizedSearchCV

parameters={'n_estimators':range(10, 300, 10), 'criterion':['mse', 'mae'], 
            'max_features':['auto', 'sqrt', 'log2']}

rs = RandomizedSearchCV(rf, parameters, scoring='neg_mean_absolute_error', cv=3)
rs.fit(X_train, y_train)

rs.best_params_
rs.best_score_

# test models
lm = LinearRegression()
lm.fit(X_train, y_train)
y_pred_lm = lm.predict(X_test)


lasso = Lasso(alpha=0.08)
lasso.fit(X_train, y_train)
y_pred_lasso = lasso.predict(X_test)

y_pred_rf = rs.best_estimator_.predict(X_test)

from sklearn.metrics import mean_absolute_error

mae_lm = mean_absolute_error(y_test, y_pred_lm)
mea_lasso = mean_absolute_error(y_test, y_pred_lasso)
mae_rf = mean_absolute_error(y_test, y_pred_rf)
