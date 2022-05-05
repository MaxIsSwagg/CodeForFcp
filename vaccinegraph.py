#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May  3 13:35:27 2022

@author: edatkinson
"""

import pandas as pd
import matplotlib.pyplot as plt

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
