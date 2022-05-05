#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May  5 18:41:27 2022

@author: maxchesters
"""

import pandas as pd
import matplotlib.pyplot as plt
#<<<<<<< HEAD
import numpy as np
from matplotlib.animation import FuncAnimation

vaccine_check = input('Do you want to see an animated graph of vaccine data(Y/N):')
if(vaccine_check == 'Y'):
    
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