# How do I parse a tab delimited file that may have values across multiple lines?
import csv
r=csv.reader(open("a.tsv"), delimiter="\t", quotechar='"')
print r.next()
