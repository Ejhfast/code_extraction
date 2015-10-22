# dictionary to read 3 values from a csv file in python
mydict = dict((rows[0],rows[1:]) for rows in reader)
