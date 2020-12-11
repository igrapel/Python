import random 
import time
import matplotlib.pyplot as plt

tickets = []
num_tickets = int(input("How many tickets? "))

for ticket in range(num_tickets):
    t = random.randint(1, 999)
    tickets.append(t)


tickets.sort()
#print(tickets)    
#print(tickets)

#Linear Search/Sequential Search Efficiency
#O(N) ~ N
def linear_search(num):
    for i in range(num_tickets):
        if(num == tickets[i]):
            return i
    return -1

def binary_search(num):
    low = 0
    high = len(tickets) - 1
    mid = 0
    
    while(low<=high):
        mid = (low + high) // 2
        
        if(tickets[mid] < num):
            low = mid + 1
        
        elif(tickets[mid] > num):
            high = mid - 1
            
        else:
            return mid

    return -1

start = time.perf_counter()
print("Binary Test: ", binary_search(-54))
end = time.perf_counter()
time_spent = end - start
print("Binary Search Time: " + "{:.6f}".format(time_spent) + " seconds")

binary_times = [.000101, .000226, 0.000125, .000158, 0.000715]
inputs = [1000, 10000, 100000, 500000, 1000000]
linear_times = [.000227, .000630, .005778, 0.027184,  0.055743]

"""
start = time.perf_counter()
print("Linear Test: ", linear_search(-54))
end = time.perf_counter()
time_spent = end - start
print("Linear Search Time: " + "{:.6f}".format(time_spent) + " seconds")
"""

inputs = [1000, 10000, 100000, 500000, 1000000]
linear_times = [.000227, .000630, .005778, 0.027184,  0.055743]
binary_times = [.000101, .000226, 0.000125, .000158, 0.000715]
plt.scatter(inputs, linear_times)
plt.scatter(inputs, binary_times, color='#de88c1')
plt.show()
