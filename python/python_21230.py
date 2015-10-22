# Storing a list of strings to a HDF5 Dataset from Python
asciiList = [n.encode("ascii", "ignore") for n in strList]
h5File.create_dataset('xxx', (len(asciiList),1),'S10', asciiList)
