# -*- coding: utf-8 -*-
"""
Created on Thu Jun 13 19:24:57 2019

@author: Jorge
"""

import pandas as pd

df = pd.read_csv('athlete_events.csv')

print(df.describe())