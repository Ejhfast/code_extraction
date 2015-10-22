# Python, load .csv in numpy arrays, return a list
import numpy as np
X, Y, Z = np.genfromtxt('targets.csv', delimiter=',', unpack=True)
