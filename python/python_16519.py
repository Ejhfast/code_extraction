# Python find sum of column in table in text file
import numpy
data = numpy.loadtxt('filename.txt')
print(data[7:,1].sum())
