# Changing the column order
(customerno, firstname, lastname, sales) = line
outLine = (sales, firstname, lastname, customerno)
output.writerow(outLine)
