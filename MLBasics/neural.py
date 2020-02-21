 First set up the network.
sigma = np.tanh
W = np.array([[-2, 4, -1],[6, 0, -3]])
b = np.array([0.1, -2.5])

# Define our input vector
x = np.array([0.3, 0.4, 0.1])


def a1(a0):
     return sigma(np.matmul(W, a0)+b)

a1_0, a1_1=a1(x)

# Calculate the values by hand,
# and replace a1_0 and a1_1 here (to 2 decimal places)
# (Or if you feel adventurous, find the values with code!)

a1 = np.array([a1_0, a1_1])
