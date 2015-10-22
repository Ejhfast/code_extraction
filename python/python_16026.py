# How can I identify the column with the greatest average in a numpy array?
numpy.argmax(numpy.average(complete_matrix,axis=0, weights=complete_matrix!=0))
