#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 26 14:32:41 2022

@author: mehdiamara
"""

import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

from matplotlib.animation import FuncAnimation



""" 
THIS HAS TO BE RUN THROUGH THE TERMINAL FOR THE ANIMATION TO SHOW UP
"""



# Total population, N.
N = 1000
# Initial number of infected and recovered individuals, I0 and R0.
I0, R0 = 1, 0
# Everyone else, S0, is susceptible to infection initially.
S0 = N - I0 - R0
# Contact rate, beta, and mean recovery rate, gamma, (in 1/days).
beta, gamma = 0.2, 1./10 
# A grid of time points (in days)
t = np.linspace(0, 160, 160)

# The SIR model differential equations.
def deriv(y, t, N, beta, gamma):
    S, I, R = y
    dSdt = -beta * S * I / N
    dIdt = beta * S * I / N - gamma * I
    dRdt = gamma * I
    return dSdt, dIdt, dRdt

# Initial conditions vector
y0 = S0, I0, R0
# Integrate the SIR equations over the time grid, t.
ret = odeint(deriv, y0, t, args=(N, beta, gamma))
S, I, R = ret.T

# Plot the data on three separate curves for S(t), I(t) and R(t)
# fig = plt.figure(facecolor='w')
# ax = fig.add_subplot(111, facecolor='#dddddd', axisbelow=True)
# ax.plot(t, S/1000, 'b', alpha=0.5, lw=2, label='Susceptible')
# ax.plot(t, I/1000, 'r', alpha=0.5, lw=2, label='Infected')
# ax.plot(t, R/1000, 'g', alpha=0.5, lw=2, label='Recovered with immunity')
# ax.set_xlabel('Time /days')
# ax.set_ylabel('Number (1000s)')
# ax.set_ylim(0,1.2)
# ax.yaxis.set_tick_params(length=0)
# ax.xaxis.set_tick_params(length=0)

# ax.grid(b=True, which='major', c='w', lw=2, ls='-')
# legend = ax.legend()
# legend.get_frame().set_alpha(0.5)
# for spine in ('top', 'right', 'bottom', 'left'):
#     ax.spines[spine].set_visible(False)


x = []
y1 = []
y2 = []
y3 = []


figure = plt.figure(facecolor='w')
ax = plt.axes(xlim=(0, 160), ylim=(0, 1.2))
# ax.set_xlim(0, 160) 
# ax.set_ylim(0, 1.2)
plt.xlabel('Time (in days)')
plt.ylabel('Number (in thousands)')


# ax.grid(b=True, which='major', c='w', lw=2, ls='-')
# legend = ax.legend()
# legend.get_frame().set_alpha(0.5)
for spine in ('top', 'right', 'bottom', 'left'):
    ax.spines[spine].set_visible(False)


# line,  = ax.plot(0, 0)
plotlays, plotcols = [3], ["blue", "red", "green"]
lines = []
for index in range(3):
    lobj = ax.plot([],[],lw=2,color=plotcols[index])[0]
    lines.append(lobj)



def init():
    for line in lines:
        line.set_data([],[])
    return lines



x = []
y1 = []
y2 = []
y3 = []


def animate(i): 
    t = np.linspace(0, 160, 160)
    y_S = S/1000
    y_I = I/1000
    y_R = R/1000
    
    x.append(t[i]) 
    y1.append(y_S[i])
    y2.append(y_I[i])
    y3.append(y_R[i])
    
    ylist = [y1, y2, y3]
  
    for lnum,line in enumerate(lines):
        line.set_data(x, ylist[lnum]) # set data for each line separately. 
    
    # for index in range(0, 2):
    #     line.set_data(x, ylist[index])
        
    return lines


line_drawer = FuncAnimation(figure, func = animate, init_func=init, frames = 160,  interval = 5, repeat=False) 

plt.grid()
plt.show()





