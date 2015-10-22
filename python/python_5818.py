# Numpy index out of range error
import datetime
fixdate = lambda d: datetime.datetime.strptime(d, '%d/%m/%Y')
r = mlab.csv2rec(datafile, delimiter=';', converterd={0: fixdate})
