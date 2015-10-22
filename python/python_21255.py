# Python: Write a list of numeric values on a single row with a repeated format
s = ('{:10.4f} '*len(draw6)).format(*draw6)    # s = '    0.1323     0.1424     0.1524     0.1623'
file.write(s)
