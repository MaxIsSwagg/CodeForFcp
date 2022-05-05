#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 29 13:25:06 2022

@author: maxchesters
"""

import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

from matplotlib.animation import FuncAnimation

"""
This has to be run through the terminal for the animated plot to show up
"""
Animate_Check = input('Would you like to run an sird model to compare(Y/N):')
if (Animate_Check == 'Y'):
    N = int(input('Enter population size: ')) 
    I0 =  int(input('Enter the number of initial infected people: ')) 
    R0 = int(input('How many people are already recovered: ')) 
    D0 = int(input('How many people are already dead: ')) 
    S0 = N - I0 - R0 - D0
    beta = float(input('Enter your contact rate (How many infected people come into contact with other individuals per unit time): ')) 
    gamma = float(input('Enter mean recovery rate (1/ days to recover): ')) 
    K = float(input('Enter the proportion of how many infected die: '))
    time_frame = int(input('Please enter your time frame (days): ')) 
    
    # Example of working values:
    # N = 1000
    # I0 = 1
    # R0 = 0
    # D0 = 0
    # S0 = N - I0 - R0 - D0
    # beta = 0.4
    # gamma = 0.1
    # K = 0.05
    # time_frame = 160
    
    t= np.linspace(0, time_frame, time_frame )
    
    
    
    def deriv(y, t, N, beta, gamma, K):
        S, I, R, D = y
        dSdt =  -beta * S * I / N 
        dIdt = beta * S * I / N - gamma * I - K * I
        dRdt = gamma * I
        dDdt = K * I
        return dSdt, dIdt, dRdt, dDdt
    
    
    y0 = S0, I0, R0, D0
    
    ret = odeint(deriv, y0, t, args=(N, beta, gamma, K))
    S, I, R, D = ret.T
    
    # fig = plt.figure(facecolor='w')
    # ax = fig.add_subplot(111, facecolor='#dddddd', axisbelow=True)
    # ax.plot(t, S/N, 'b', alpha=0.5, lw=2, label='Susceptible')
    # ax.plot(t, I/N, 'r', alpha=0.5, lw=2, label='Infected')
    # ax.plot(t, R/N, 'g', alpha=0.5, lw=2, label='Recovered with immunity')
    # ax.plot(t, D/N, 'y', alpha=0.5, lw=2, label='Dead')
    # ax.set_xlabel('Time /days')
    # ax.set_ylabel('percentage of population ')
    # ax.set_ylim(0,1.2)
    # ax.yaxis.set_tick_params(length=0)
    # ax.xaxis.set_tick_params(length=0)
    # ax.grid(b=True, which='major', c='w', lw=2, ls='-')
    # legend = ax.legend()
    # legend.get_frame().set_alpha(0.5)
    # for spine in ('top', 'right', 'bottom', 'left'):
    #     ax.spines[spine].set_visible(False)
    # plt.show()
    
    figure = plt.figure(facecolor='w')
    ax = plt.axes(xlim=(0, 160), ylim=(0, 1.2))
    plt.xlabel('Time (in days)')
    plt.ylabel('Percentage of population')
    
    
    
    plotlays, plotcols = [4], ["blue", "red", "green", "black"]
    lines = []
    for index in range(4):
        lobj = ax.plot([],[],lw=2,color=plotcols[index])[0]
        lines.append(lobj)
        
    labels = plotcols
    f = lambda m,c: plt.plot([],[],marker=m, color=c, ls="none")[0]
    handles = [f("s", plotcols[i]) for i in range(3)]
    legend = plt.legend(handles, labels, loc=3, framealpha=1, frameon=False)    
    
    def init():
        for line in lines:
            line.set_data([],[])
        return lines
    
    ax.legend((lines), ('Susceptible', 'Infected', 'Recovered', 'Dead'), loc='upper right', shadow=True)
    
    
    x = []
    y1 = []
    y2 = []
    y3 = []
    y4 = []
    
    
    
    def animate(i): 
        t = np.linspace(0, time_frame, time_frame)
        y_S = S/N
        y_I = I/N
        y_R = R/N
        y_D = D/N
        
        x.append(t[i]) 
        y1.append(y_S[i])
        y2.append(y_I[i])
        y3.append(y_R[i])
        y4.append(y_D[i])
        
        ylist = [y1, y2, y3, y4]
      
        for lnum,line in enumerate(lines):
            line.set_data(x, ylist[lnum]) # set data for each line separately. 
        
        # for index in range(0, 2):
        #     line.set_data(x, ylist[index])
            
        return lines
    
    
    line_drawer = FuncAnimation(figure, func = animate, init_func=init, frames = 160,  interval = 5, repeat=False) 
    
    plt.grid()
    plt.show()


  
  
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
