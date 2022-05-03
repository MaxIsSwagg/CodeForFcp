#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 29 14:52:15 2022

@author: maxchesters
"""

import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
import math

GREY = (0.78, 0.78, 0.78)  # uninfected
RED = (0.96, 0.15, 0.15)   # infected
GREEN = (0, 0.86, 0.03)    # recovered
BLACK = (0, 0, 0)          # dead


r0 = 1.2 #how many people get it in 1 days

death = 14 #in days
chance_death = 0.05 #percentage
time = 100 # length of pandemic




initial_population = 5000000000 #susceptible people
S0 = 0

I0 = 1000000 # initial infected
I1 = 1 #place holder for list of new infections
R0 = 0 #initial recovered
R1 = 0 #place holder for new recoveries per day
D0 = 0 #initial dead
D1 = 0 #placeholder for calculating recovered each day


Infected_new = []
Infected_new.append(I0)
Recovered=[]
Dead = []
Infected = []
image = []
days = []
susceptible= []

all_infected = False

end = False

for x in range (1, time):
    if( I0+R0+D0 < initial_population and all_infected == False ):
        I0 = math.ceil(I0 * r0)
        if (I0+R0+D0 > initial_population):
            I0 = initial_population - (R0+D0)
            all_infected = True
    
        
        
        
    else:
        all_infected = True
   
    
    if (end == False):
        
        if (x < death):
            Infected_new.append(I0 - I1) # uploads value for new infected today
            I1 = I0 
        
    
        if( x >= death):
            
            if((I0 + R0 + D0) == initial_population and (Infected_new[x - death]) <= 0  ):
                D1 = math.floor(I0 * chance_death)
                D0 = D0 + D1
                R0 = R0 + (I0 - D1)
                I0 = 0
                end = True
            
            else:
            
            
                D1 =  math.floor((Infected_new[x - death]) * chance_death )
                D0 = D0 + D1
                R0 = R0 + ((Infected_new[x - death]) - D1)
                I0 = I0 - Infected_new[x - death]
        
            if(I0 - I1 >= 0):
                Infected_new.append(I0 - I1)  
                I1 = I0
            else:
                Infected_new.append(0)
    
            
        
         
        
            
    Infected.append(I0)
    Dead.append(D0)        
    Recovered.append(R0)
    days.append(x)   
    susceptible.append(initial_population-(I0+R0+D0))    
    
    
    rgb_matrix = []
    percentage_infected = math.floor((I0 / initial_population)* 10000)
    percentage_recovered = math.floor((R0 / initial_population)* 10000)
    percentage_dead = math.floor((D0 / initial_population)* 10000)
    percentage_susceptible = 10000 - (percentage_dead + percentage_recovered + percentage_infected )
    
    for s in range (0, (percentage_susceptible)):
        rgb_matrix.append(GREY)
    
    for i in range (0, (percentage_infected)):
        rgb_matrix.append(RED)
    
    for r in range (0, (percentage_recovered)):
        rgb_matrix.append(GREEN)
    
    for d in range (0, (percentage_dead)):
        rgb_matrix.append(BLACK)
    
    np.random.shuffle(rgb_matrix)    
    rgb_image = np.reshape(rgb_matrix,(100,100,3))
    image.append(rgb_image)    
                    
     # total for day before
   
print(Infected_new)
print('----')


def animate_func(i):
    im.set_array(image[i])
    return [im]

fps = 30



fig = plt.figure(figsize = (10,10))
plt.title("Pandemic Spreading with Random Movement")
plt.xticks([])
plt.yticks([])

im = plt.imshow(image[0], interpolation='none', aspect='auto', vmin=0, vmax=1)

anim = animation.FuncAnimation(
                               fig, 
                               animate_func, 
                               frames = time,
                               interval = 1000 / fps, # in ms
                               )

fig2 = plt.figure(facecolor='w')
ax = fig2.add_subplot(111, facecolor='#dddddd', axisbelow=True)
ax.plot(days, Infected, 'r', alpha=0.5, lw=2, label='Infected')
ax.plot(days, Recovered, 'g', alpha=0.5, lw=2, label='Recovered')
ax.plot(days, Dead, 'black', alpha=0.5, lw=2, label='Dead')
ax.plot(days, susceptible, 'grey', alpha=0.5, lw=2, label='Susceptible')
ax.set_xlabel('Time /days')
ax.set_ylabel('population')
ax.set_ylim(0,initial_population)
ax.yaxis.set_tick_params(length=0)
ax.xaxis.set_tick_params(length=0)
ax.grid(b=True, which='major', c='w', lw=2, ls='-')
legend = ax.legend()
legend.get_frame().set_alpha(0.5)
for spine in ('top', 'right', 'bottom', 'left'):
    ax.spines[spine].set_visible(False)
plt.show()




