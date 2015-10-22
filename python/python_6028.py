# Continue reading rows in a for loop despite of null values in a row
reader = csv.reader( (line.replace('\0','') for line in f) , delimiter=';',quotechar = '"')
