# Python: How to write a dictionary of tuple values to a csv file?
import csv
with open("data.csv", "wb") as f:
    csv.writer(f).writerows((k,) + v for k, v in maxDict.iteritems())
