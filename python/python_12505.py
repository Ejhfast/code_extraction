# Can numpy.savetxt be used on N-dimensional ndarrays with N>2?
myarray = rand(5,5,5)
name = 'myarray'+myarray.shape+'.txt'
np.savetxt(name,myarray.flatten())
