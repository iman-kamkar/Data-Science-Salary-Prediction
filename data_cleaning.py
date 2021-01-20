#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 20 14:09:17 2020

@author: iman
"""
import pandas as pd
import re 
data = pd.read_csv('glassdoor.csv') 
df = data.copy()

## Todo list
# compute the min, max and average salary
# company name text only
# Location state only
# age of the company

######## SALARY
#convert all column names to lowercase
df.columns = df.columns.str.lower()

#Remove rows without salary or job description
to_drop = df[(df['job description'] == '-1') | (df['salary estimate'] == '-1')].index
df.drop(to_drop, axis=0, inplace=True)

df['hourly'] = df['salary estimate'].apply(lambda x: 1 if 'per hour' in x.lower() else 0)

df['employer_provided'] = df['salary estimate'].apply(lambda x: 1 if 'employer provided salary:' in x.lower() else 0)




# remove the $ and 'K' signs and convert string values to integer
salary = df['salary estimate'].apply(lambda x: re.findall('\$*[0-9]*K*-\$*[0-9]*K*', x)[0]).\
    apply(lambda x: x.replace('$', '')).apply(lambda x: x.replace('K', '')).str.split('-', expand=True).astype(int)


df['min_salary'] = salary[0]
df['max_salary'] = salary[1]
df['avg_salary'] = salary.mean(axis=1)

########### COMPANY NAME ONLY

df['company_txt']  = df['company name'].apply(lambda x: x.split('\n')[0])

######## STATE FIELD
df['job_state'] = df['location'].str.split(',').apply(lambda x: x[0].strip() if len(x)==1 else x[1].strip())

state_df = pd.read_csv('states.csv')

def replace_state(name):
    if state_df['State'].str.contains(name).any():
        i = state_df[state_df['State'] == name].index.values[0]
        return state_df.iloc[i]['Abbreviation']
    else:
        return name
    
    
df['job_state'] = df['job_state'].apply(lambda x: x if len(x)==2 else replace_state(x))

######## COMPANY AGE

df['age'] = df['founded'].apply(lambda x: x if x<1 else 2020-x)

######## PARSING JOB DESCRIPTION
#parsing of job description (python, etc)
#python
df['python_yn'] = df['job description'].apply(lambda x: 1 if 'python' in x.lower() else 0)
print(df.python_yn.value_counts())
 
#r studio 
df['R_yn'] = df['job description'].apply(lambda x: 1 if 'r studio' in x.lower() or 'r-studio' in x.lower() else 0)
print(df.R_yn.value_counts())

#spark 
df['spark'] = df['job description'].apply(lambda x: 1 if 'spark' in x.lower() else 0)
df.spark.value_counts()

#aws 
df['aws'] = df['job description'].apply(lambda x: 1 if 'aws' in x.lower() else 0)
df.aws.value_counts()

#excel
df['excel'] = df['job description'].apply(lambda x: 1 if 'excel' in x.lower() else 0)
df.excel.value_counts()


df_out = df.drop(['unnamed: 0'], axis =1)

df_out.to_csv('salary_data_cleaned.csv',index = False)










