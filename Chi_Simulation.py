# -*- coding: utf-8 -*-
"""
Created on Wed Jun  2 20:04:34 2021

@author: ilang
"""

import random
import numpy as np
import matplotlib.pyplot as plt

proportions = [.2, .3, .4, .1]

#convert list to cumulative
def to_cumulative(prop_list):
    sum_proportions = 0
    cumulative = []
    for prop in prop_list:
        sum_proportions += prop
        cumulative.append(sum_proportions)
    return cumulative

#Parameters: list of proportions and number of trials
def simulate_chi(p_list, num):
    colors = [0]*len(p_list)
    p_list = to_cumulative(p_list)
    for experiment in range(num):
        p = random.uniform(0, 1)
        elements = len(p_list)-2
        while(elements >= 0):
            if(p_list[elements] < p):
                colors[elements+1] +=1
                break
            elements -=1
        if(elements==-1):
            colors[elements+1] +=1  
    return colors

sim = simulate_chi(proportions, 100)              
print(sim)

#Create Bar Plot
expected = [element * 100 for element in proportions]
data = [expected, sim]
X = np.arange(len(proportions))
fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
ax.bar(X + 0.00, data[0], color = 'b', width = 0.25, label="Expected")
ax.bar(X + 0.25, data[1], color = 'g', width = 0.25, label="Simulated")


ax.set_xticks(X)
ax.set_xticklabels(["Group 1", "Group 2", "Group 3", "Group 4"])
ax.legend()





