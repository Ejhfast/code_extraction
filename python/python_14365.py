# Frequency tables in pandas (like plyr in R)
d1.groupby('ExamenYear').agg({'Participated': len,
                              'Passed': lambda x: sum(x == 'yes')})
