#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May  3 13:35:27 2022

@author: edatkinson
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation



df = pd.read_csv("vaccinations.csv")
df.plot(x = 'Days ', y = ['total_vaccinations', 'people_vaccinated', 'people_fully_vaccinated'])



plt.style.use('seaborn')
fig = plt.figure()
ax = fig.add_subplot(1,1,1)


def animation(i):
  vaccinationsdata = pd.read_csv('vaccinations.csv')
  x = []
  y = []
  x = vaccinationsdata[0:i]['Days ']
  y = vaccinationsdata[0:i]['total_vaccinations']
  
  ax.clear()
  ax.plot(x, y)


animation = FuncAnimation(fig, func=animation, interval=1000)
plt.show()
