# Python sniffer for 2 different CSV-types
dialect = csv.Sniffer().sniff(csvfile.readline(), [',',';'])
csvfile.seek(0)
data = csv.reader(csvfile, dialect)
