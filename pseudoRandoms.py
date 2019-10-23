# -*- coding: utf-8 -*-
"""
Created on Fri Oct 18 07:57:59 2019
@author: 323917
"""
import numpy as np
import matplotlib.pyplot as plt

import random

"""
randomList=[]
for x in range(12000):
    randInt=random.randint(1,10)
    randomList.append(randInt)
    
counts = []
for x in range(10):
    countDig = randomList.count(x)
    counts.append(countDig)
     
objects = ('0','1', '2', '3', '4', '5', '6', '7', '8', '9')
y_pos = np.arange(len(objects))
plt.bar(y_pos, counts, align='center', alpha=0.5)
plt.xticks(y_pos, objects)
plt.ylabel('Counts')
plt.title('Digits')
plt.show()
"""
def getnumber():
    while True:
        number = input("Give me a digit: ")
        if number.isdigit():
            return int(number)
        
        
n_groups = 10
objects = ('0','1', '2', '3', '4', '5', '6', '7', '8', '9')

randomList=[]
studentList=[]

num_Questions = int(input("How many digits to produce?" ))

for x in range(num_Questions):
    randInt=random.randint(0,9)
    randomList.append(randInt)
    
Random_counts = []
for x in range(10):
    countDig = randomList.count(x)
    Random_counts.append(countDig)

test = input("Ask the students? ")


if(test=="no"):
    
    for x in range(num_Questions):
        randInt=random.randint(1,10)
        studentList.append(randInt)
    
    Student_counts=[]

    for x in range(10):
        count_studentDigit=studentList.count(x)
        Student_counts.append(count_studentDigit)    

else:
    for num in range(num_Questions):
        studentNum= getnumber()

        studentList.append(studentNum)
        
        Student_counts=[]

    for x in range(10):
        count_studentDigit=studentList.count(x)
        Student_counts.append(count_studentDigit)    



# create plot
fig, ax = plt.subplots()
index = np.arange(n_groups)
bar_width = 0.35
opacity = 0.8

rects1 = plt.bar(index, Random_counts, bar_width,
alpha=opacity,
color='b',
label='Random')

rects2 = plt.bar(index + bar_width,Student_counts , bar_width,
alpha=opacity,
color='g',
label='Students')

plt.xlabel('Digit')
plt.ylabel('Count')
plt.title('Pseudo v Random')
plt.xticks(index + bar_width, objects)
plt.legend()

plt.tight_layout()
plt.show()
