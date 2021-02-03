#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb  3 12:14:20 2021

@author: iman
"""
import requests
from data_input import data_in

url = 'http://127.0.0.1:5000/predict'
headers = {"Content_Type": "application/json"}
data = {"data": data_in}

r = requests.get(url, headers=headers, json=data)

r.json()
