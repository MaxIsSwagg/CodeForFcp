#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May  3 12:21:14 2022

@author: edwardloughrey
"""

import pandas as pd
import matplotlib.pyplot as plt
import os.path

DataFrameCheck = input("Would you like to enter csv  data  to plot graphs? (Y/N): ")


    


"""
This piece of code will allow you to enter the csv files attatched or your own csv files
and create a data frame and then plot this data which can be compared to the plots in the model
"""
 

def DataFrameInput():
    


    print('This program is going to compile data you have to create plots to compare against the model')
    
    
    RepeatFileInput = True #sets a variable to repeat the loop if an incorrect input is given
    
    while (RepeatFileInput == True):
        
        file_input = str(input('please enter file for cases(including file path):'))
        file_exist = os.path.exists(file_input) #  checking for file
        if (file_exist == True):  
            dF_covid = pd.read_csv(file_input, sep = ',')
            dF_length = dF_covid
            RepeatFileInput = False 
        else:
            print('your file does not exist, please try again') 
    
    # Naming columns
    dF_covid.columns = ['Date', 'Cases']
    dF_covid.index = dF_covid['Date']
    dF_covid.pop('Date')
           
    
    expand_dF = (input('Would you like to add more columns (True/False):'))
    
    while (expand_dF == 'True'): #  another loop to make up for user errors
        column_addition = str(input('please enter a file name(including file path):'))
        file_exist = os.path.exists(column_addition)
        if (file_exist == True):
            extra_column = pd.read_csv(column_addition, sep = ',')
            column_name =  input('Please enter the name of your extra column:')
            
            # adds new column to dataframe
            extra_column.columns = ['Date', column_name] 
            extra_column.index  = extra_column['Date']
            extra_column.pop('Date')
            
            dF_covid[column_name] = extra_column[column_name]
            
            expand_dF = (input('Would you like to add more columns (True/False):'))
        else:
            print('your file does not exist, please try again')
    
    
    # Creates a Time column as is easier to deal with a number of days, than a bunch of separate dates 
    dF_covid.fillna(0)
    time = []
    for x in range (0, len(dF_covid.index)):
        time.append(x)
        
    dF_covid["Time"] = time
    
    print(dF_covid)
    
    
    
    # makes a list of the column names
    allColumns = dF_covid.columns.values.tolist()
    columns_noTime = allColumns.pop()
    # print(allColumns, ", ", columns_noTime)
    
    dF_covid.plot(x='Time', y=allColumns)
    plt.ylabel("Population")
    
        
        
    
    
    """
    The code that follows (for uk data) will highlight the key dates of rule/policy changes and
    label them appropriately.
    """
    
    
    
    if file_input == 'data_cases_england.csv':     # DEPENDS ON THE FILE NAME
        uk_dates = input(str("Would you like to highlight UK restriction periods? (Y/N): "))
        while uk_dates != 'Y' and uk_dates != 'N':
            uk_dates = input(str("ERROR: Would you like to highlight UK restriction periods? (Y/N): "))
        
    
    
        # section applies if user wants to see key dates
    if uk_dates == 'Y':
           
            # Making coloured sections
        plt.axvspan(0, 94, facecolor='purple', alpha=0.2)      # First lockdown
        plt.axvspan(94, 218, facecolor='yellow', alpha=0.2)      # Pubs open
        plt.axvspan(218, 245, facecolor='purple', alpha=0.2)   # 2nd national lockdown (with schools still open)
        plt.axvspan(245, 280, facecolor='red', alpha=0.3)      # Tier system introduced
        plt.axvspan(280, 341, facecolor='purple', alpha=0.2)   # 3rd national lockdown
        plt.axvspan(341, 375, facecolor='red', alpha=0.3)      # Schools return
        plt.axvspan(375, 473, facecolor='yellow', alpha=0.2)     # Pubs open
    
    
        # If data for tests is included, the graph is greatly apmplified. So the labelling is
        # different for each version of the line graph
        
        if "Tests" in allColumns:
            plt.text(0, 140000, "1st Lockdown", fontdict=None, fontsize='x-small')
            plt.text(94, 285000, "Restrictions Eased", fontdict=None, fontsize='x-small')
            plt.text(218, 750000, "2nd Lockdown", fontdict=None, fontsize='x-small')
            plt.text(245, 1000000, "Tiers Introduced", fontdict=None, fontsize='x-small')
            plt.text(280, 1575000, "3rd Lockdown", fontdict=None, fontsize='x-small')
            plt.text(341, 1875000, "Schools Return", fontdict=None, fontsize='x-small')
            plt.text(375, 275000, "Restrictions Eased", fontdict=None, fontsize='x-small')
            plt.text(473, 175000, "All Restrictions Lifted", fontdict=None, fontsize='x-small')
        
        
        # Labelling sections for when the 'Vaccinations' column is involved
        # Would be better if this linked to actual file name
        elif "Vaccinations" in allColumns:
            plt.text(0, 15000, "1st Lockdown", fontdict=None, fontsize='x-small')
            plt.text(94, 30000, "Restrictions Eased", fontdict=None, fontsize='x-small')
            plt.text(218, 75000, "2nd Lockdown", fontdict=None, fontsize='x-small')
            plt.text(245, 115000, "Tiers Introduced", fontdict=None, fontsize='x-small')
            plt.text(280, 157500, "3rd Lockdown", fontdict=None, fontsize='x-small')
            plt.text(341, 187500, "Schools Return", fontdict=None, fontsize='x-small')
            plt.text(375, 475000, "Restrictions Eased", fontdict=None, fontsize='x-small')
            plt.text(473, 425000, "All Restrictions Lifted", fontdict=None, fontsize='x-small')
        else:
            plt.text(0, 10000, "1st Lockdown", fontdict=None, fontsize='x-small')
            plt.text(94, 18000, "Restrictions Eased", fontdict=None, fontsize='x-small')
            plt.text(218, 80000, "2nd Lockdown", fontdict=None, fontsize='x-small')
            plt.text(245, 90000, "Tiers Introduced", fontdict=None, fontsize='x-small')
            plt.text(280, 60000, "3rd Lockdown", fontdict=None, fontsize='x-small')
            plt.text(341, 50000, "Schools Return", fontdict=None, fontsize='x-small')
            plt.text(375, 40000, "Restrictions Eased", fontdict=None, fontsize='x-small')
            plt.text(473, 8000, "All Restrictions Lifted", fontdict=None, fontsize='x-small')
    
    
    plt.show()





if (DataFrameCheck  == 'Y'):
    DataFrameInput()




