# Use Distance Matrix in scipy.cluster.hierarchy.linkage()?
import scipy.spatial.distance as ssd
# convert the redundant n*n square matrix form into a condensed nC2 array
    distArray = ssd.squareform(distMatrix) # distArray[{n choose 2}-{n-i choose 2} + (j-i-1)] is the distance between points i and j
