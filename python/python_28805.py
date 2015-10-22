# Better way to pack numpy array?
X = numpy.array([[1,2,3],[4,5,6]])
b = struct.pack('=%sf' % X.size, *X.flatten('F'))
