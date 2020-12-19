#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 16 14:10:01 2020

@author: iman
"""
import glassdoor_scraper as gs
import pandas as pd

path = "/Volumes/Macintosh Data/Data Science/my_projects/ds_salary_project/chromedriver"

df = gs.get_jobs('data scientist', 1000, False, path, 15)
df.to_csv(r'glassdoor.csv')