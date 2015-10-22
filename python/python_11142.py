# Define row of CSV file if row contains specific string
import csv
rows = csv.reader(open('yourfile.csv', 'rb'), delimiter=' ', quotechar='|')
arows = [row for row in rows if 'a' in row]
