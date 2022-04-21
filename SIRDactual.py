#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 29 13:25:06 2022

@author: maxchesters
"""

import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

N = int(input('Enter population size: '))
I0 = int(input('Enter the number of initial infected people: '))
R0 = int(input('How many people are already recovered: '))
D0 = int(input('How many people are already dead: '))
S0 = N - I0 - R0 - D0
beta = float(input('Enter your contact rate (How many infected people come into contact with other individuals per unit time): '))
gamma = float(input('Enter mean recovery rate (1/ days to recover): '))
K = float(input('Enter the proportion of how many infected die: '))
time_frame = int(input('Please enter your time frame (days): '))

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

fig = plt.figure(facecolor='w')
ax = fig.add_subplot(111, facecolor='#dddddd', axisbelow=True)
ax.plot(t, S/N, 'b', alpha=0.5, lw=2, label='Susceptible')
ax.plot(t, I/N, 'r', alpha=0.5, lw=2, label='Infected')
ax.plot(t, R/N, 'g', alpha=0.5, lw=2, label='Recovered with immunity')
ax.plot(t, D/N, 'y', alpha=0.5, lw=2, label='Dead')
ax.set_xlabel('Time /days')
ax.set_ylabel('percentage of population ')
ax.set_ylim(0,1.2)
ax.yaxis.set_tick_params(length=0)
ax.xaxis.set_tick_params(length=0)
ax.grid(b=True, which='major', c='w', lw=2, ls='-')
legend = ax.legend()
legend.get_frame().set_alpha(0.5)
for spine in ('top', 'right', 'bottom', 'left'):
    ax.spines[spine].set_visible(False)
plt.show()