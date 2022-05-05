#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May  3 14:16:15 2022

@author: maxchesters
"""
"""
This is our main code that will run everything
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

def matrix_append (percentage, colour):
    for s in range (0, (percentage)):
        rgb_matrix.append(colour)


initial_population = 5000000000 #susceptible people
S0 = 0

I0 = 1000000 # initial infected
I1 = 1 #place holder for list of new infections
R0 = 0 #initial recovered
R1 = 0 #place holder for new recoveries per day
D0 = 0 #initial dead
D1 = 0 #placeholder for calculating recovered each day


Infected_new = [] 
Infected_new.append(I0) #list of new infected per day
Recovered=[] 
Dead = []    #list of total recovered dead susceptible and infected 
Infected = []
susceptible= []
image = [] #stores images as a list
days = [] #counts days


all_infected = False # boolean for if everyone has been infected

end = False

for x in range (1, time):
    if( I0+R0+D0 < initial_population and all_infected == False ):
        I0 = math.ceil(I0 * r0)     # infected multiplied by how many they infect each day
        if (I0+R0+D0 > initial_population):
            I0 = initial_population - (R0+D0)  #keeps variables within size of population
            all_infected = True
    
        
        
        
    else:
        all_infected = True
   
    
    if (end == False):
        
        if (x < death):
            Infected_new.append(I0 - I1) # uploads value for new infected today
            I1 = I0 
        
    
        if( x >= death):
            
            if((I0 + R0 + D0) == initial_population and (Infected_new[x - death]) <= 0  ):
                D1 = math.floor(I0 * chance_death)   #if the point is reached where people start to die
                D0 = D0 + D1                         #the values of recovered and dead are calculated from how long ago they were infected
                R0 = R0 + (I0 - D1)
                I0 = 0
                end = True
            
            else:
            
            
                D1 =  math.floor((Infected_new[x - death]) * chance_death )
                D0 = D0 + D1
                R0 = R0 + ((Infected_new[x - death]) - D1) #If there is no new infected people to calculate from everybody either dies or recovers
                I0 = I0 - Infected_new[x - death]
        
            if(I0 - I1 >= 0):
                Infected_new.append(I0 - I1)      #updates value for newly infected peoplle
                I1 = I0
            else:
                Infected_new.append(0)
    
            
        
         
        
            
    Infected.append(I0)
    Dead.append(D0)            #appends variables for the day to list for plotting
    Recovered.append(R0)
    days.append(x)   
    susceptible.append(initial_population-(I0+R0+D0))    
    
    
    rgb_matrix = []
    percentage_infected = math.floor((I0 / initial_population)* 10000)
    percentage_recovered = math.floor((R0 / initial_population)* 10000)      #calculates values as a percentage of 10000
    percentage_dead = math.floor((D0 / initial_population)* 10000)
    percentage_susceptible = 10000 - (percentage_dead + percentage_recovered + percentage_infected )
    
 
    
    
    matrix_append(percentage_susceptible, GREY)
    matrix_append(percentage_infected, RED)
    matrix_append(percentage_recovered, GREEN) #creates the image matrix for the day
    matrix_append(percentage_dead, BLACK)
    
    
    
    np.random.shuffle(rgb_matrix)    
    rgb_image = np.reshape(rgb_matrix,(100,100,3)) #shuffles matrix and forms it into 100 x 100 image
    image.append(rgb_image)    
                    
     # total for day before
   



def animate_func(i):
    im.set_array(image[i])      #function to create animated image
    return [im]

fps = 30



fig = plt.figure(figsize = (10,10))
plt.title("Pandemic Spreading with Random Movement") #creates figure
plt.xticks([])
plt.yticks([])

im = plt.imshow(image[0], interpolation='none', aspect='auto', vmin=0, vmax=1)

anim = animation.FuncAnimation(
                               fig, 
                               animate_func, 
                               frames = time,
                               interval = 1000 / fps, # in ms
                               repeat=False)   #animates image

# fig2 = plt.figure(facecolor='w')
# ax = fig2.add_subplot(111, facecolor='#dddddd', axisbelow=True)
# ax.plot(days, Infected, 'r', alpha=0.5, lw=2, label='Infected')
# ax.plot(days, Recovered, 'g', alpha=0.5, lw=2, label='Recovered')
# ax.plot(days, Dead, 'black', alpha=0.5, lw=2, label='Dead')
# ax.plot(days, susceptible, 'grey', alpha=0.5, lw=2, label='Susceptible')
# ax.set_xlabel('Time /days')
# ax.set_ylabel('population')
# ax.set_ylim(0,initial_population)
# ax.yaxis.set_tick_params(length=0)
# ax.xaxis.set_tick_params(length=0)
# ax.grid(b=True, which='major', c='w', lw=2, ls='-')
# legend = ax.legend()
# legend.get_frame().set_alpha(0.5)
# for spine in ('top', 'right', 'bottom', 'left'):
#     ax.spines[spine].set_visible(False)
# plt.show()


"""
UNDER HERE IS THE CODE TO ANIMATE THE PLOT
NEED TO MAKE THAT INTO A REUSABLE FUNCTION FOR EASIER USE
"""



fig2 = plt.figure(facecolor='w')
ax = plt.axes(xlim=(0, 100), ylim=(0, initial_population))
plt.xlabel('Time (in days)')     #creates graph
plt.ylabel('Population ')

plotlays, plotcols = [4], ["lightgrey", "red", "green", "black"]
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

ax.legend((lines), ('susceptible', 'Infected', 'Recovered', 'Dead'), loc='upper right', shadow=True) #legend

x = []
y1 = []    #empty lists to store plot points
y2 = []
y3 = []
y4 = []

def animate(i): 
    
    y_S = susceptible
    y_I = Infected
    y_R = Recovered
    y_D = Dead
    
    x.append(days[i])            #creates lists of graph points to animate
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

line_drawer = animation.FuncAnimation(fig2, func = animate, init_func=init, frames = 160,  interval = 1000/30, repeat=False) 

plt.grid()
plt.show()

"""
Under here you have the option to run the imported code DataFrameInputs.
This will allow you to plot the data for england only in the git hub repo and
you are able to choose what data you use.
"""





import DataFrameInputs

"""
Under here you have the option to run an SIRD model to compare
"""

import animationSIRDactual

"""
Here you are asked if you want to run the sir animation
"""


import animationSIRcode

"""
Here it asks if you want to see vaccination data the data you use should is vaccinations.csv
"""
import vaccinegraph


ContinueWithSim = input('hit enter to run the simulation')
