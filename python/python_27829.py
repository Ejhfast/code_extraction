# Export Python Arrays to Matlab
import numpy, scipy.io
your_array = a multi dimential matrix
scipy.io.savemat('your direction and name', mdict={'arr': your_array})
