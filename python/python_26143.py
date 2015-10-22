# Assign variables imported from csv
import numpy as np
x, y, z = np.loadtxt('new.csv', delimiter=',', unpack=True)
