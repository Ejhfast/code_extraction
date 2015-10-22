# Is it efficent to use lists for data reading before assigning them to a numpy array?
# To load only columns 1 (time), 19 (velocity x), and 21 (velocity z).
numpy.loadtxt('data.csv', delimiter=',', usecols=(1,19,21))
