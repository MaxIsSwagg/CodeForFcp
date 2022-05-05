#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May  3 13:35:27 2022

@author: edatkinson
"""

import pandas as pd
import matplotlib.pyplot as plt
#<<<<<<< HEAD
import numpy as np
from matplotlib.animation import FuncAnimation

plt.style.use('seaborn')
fig = plt.figure()
ax = fig.add_subplot(1,1,1)


def animation(i):
  vaccinationsdata = pd.read_csv('vaccinations.csv')
  x = []
  y = []
  y2 = []
  x = vaccinationsdata[0:i]['Days ']
  y = vaccinationsdata[0:i]['total_vaccinations']
  y2 = vaccinationsdata[0:i]['people_vaccinated']
  ax.clear()
  ax.plot(x, y, y2)


plt.title("Animation of Vaccinations Against Time")
animation = FuncAnimation(fig, func=animation, interval=1)
plt.show()
#=======

def vaccinationgraph():
    

    df = pd.read_csv("vaccinations.csv")

    df.plot(x = 'Days ', y = ['total_vaccinations', 'people_vaccinated', 'people_fully_vaccinated'])
    plt.title("Graph of Covid Vaccinations against time in the UK")
    
   
    plt.show()

def vaccinationskernaldensity():
     df = pd.read_csv("vaccinations.csv")
     df['people_vaccinated'].plot.kde()
     plt.title("Kernal Density graph")
     
     plt.show()
    


vaccinationgraph()
vaccinationskernaldensity()

'''
Kernal graph basically allows us to tell how many vaccinations were given out during a shortage of vaccinations which most effectively battles the epidemic.
'''
#>>>>>>> 179b77e2d1f68e9320fc365b1f6c161e973e1cec
