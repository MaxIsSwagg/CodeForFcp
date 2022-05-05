#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 14 19:38:19 2022

@author: maxchesters
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os.path


"""
This piece of code will allow you to enter the csv files attatched or your own csv files
and create a data frame and then plot this data which can be compared to the plots in the model
"""

 


print('This program is going to compile data you have to create plots to compare against the model')


RepeatFileInput = True #sets a variable to repeat the loop if an incorrect input is given

while (RepeatFileInput == True):
    
    file_input = str(input('please enter file for cases(including file path):'))
    file_exist = os.path.exists(file_input)
    if (file_exist == True):
        dF_covid = pd.read_csv(file_input, sep = ',')
        dF_length = dF_covid
        RepeatFileInput = False 
    else:
        print('your file does not exist, please try again') 


dF_covid.columns = ['Date', 'Cases']
dF_covid.index = dF_covid['Date']
dF_covid.pop('Date')
       

expand_dF = (input('Would you like to add more columns (Y/N):'))

while (expand_dF == 'Y'):
    column_addition = str(input('please enter a file name(including file path):'))
    file_exist = os.path.exists(column_addition)
    if (file_exist == True):
        extra_column = pd.read_csv(column_addition, sep = ',')
        column_name =  input('Please enter the name of your extra column:')
        
        extra_column.columns = ['Date', column_name]
        extra_column.index  = extra_column['Date']
        extra_column.pop('Date')
        
        dF_covid[column_name] = extra_column[column_name]
        
        expand_dF = (input('Would you like to add more columns (Y/ N):'))
    else:
        print('your file does not exist, please try again')


dF_covid.fillna(0)
time = []
for x in range (0, len(dF_covid.index)):
    time.append(x)
    
dF_covid["Time"] = time


plot_check = input('Would you like to create a graph(Y/N)')
while (plot_check == 'Y'):
    plot_list = []
    plot_number = int(input('How many parameters would you like to plot') )
    for x in range(0, plot_number):
        plot_list.append(input('Please enter column title: '))
    
    dF_covid.plot(x='Time'  , y = plot_list)
    plt.show()
    plot_check = input('Would you like to create another graph(Y/N)')
    





