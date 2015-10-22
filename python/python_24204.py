# Delete dataset attribute from HDF5 file
h5copy -p -i inputFile.h5 -o outputFile.h5 -s /inputDataSetName -d /outputDataSetName -f noattr
