# "Line contains NULL byte" in CSV reader (Python)
import codecs
csvReader = csv.reader(codecs.open('file.csv', 'rU', 'utf-16'))
