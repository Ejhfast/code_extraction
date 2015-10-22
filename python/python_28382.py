# Assigning dataframe columns in rpy2
i = dataf.colnames.index('a')
dataf[i] = dataf[i].ro + 1
