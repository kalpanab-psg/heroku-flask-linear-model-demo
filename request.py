# -*- coding: utf-8 -*-
"""
Created on Sun Jun 20 14:56:17 2021

@author: bkalp
"""
 
import requests

url = 'http://localhost:5000/predict_api'
r = requests.post(url,json={'experience':2, 'test_score':9, 'interview_score':6})

print(r.json())