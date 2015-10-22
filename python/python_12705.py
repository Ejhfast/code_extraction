# Access individual cells in csv file with python
data = []
for row in csv.reader(open('you_file.csv', 'rb'), delimiter=',')
    data.append(row)
