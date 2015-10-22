# Sort the points/coordinates of a circle into a logical sequence
from math import atan2
coorinput.sort(key=lambda c:atan2(c[0], c[1]))
