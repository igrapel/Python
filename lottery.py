# -*- coding: utf-8 -*-
"""
Created on Tue Dec  8 09:28:48 2020

@author: 323917
"""
import datetime
import random
import matplotlib as plt


class lottery:
    
    def __init__(self, year, month, day):
        self.date = datetime.datetime(year, month, day)
        self.tickets = []
        
    def lottery_run(self, num_of_tickets):
        
        for index in range(num_of_tickets):
            self.tickets.append(random.randint(100,999))
            
    def linear_search(self, n):
        for index in range(len(self.tickets)):
            if(n==self.tickets[index]):
                return index
        return -1
                
        
may1 = lottery(2020, 4, 3)
may1.lottery_run(20)
print(may1.tickets)

print(may1.linear_search(200))


plt.pyplot.hist(may1.tickets, 5)
