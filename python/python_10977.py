# Handle with European date format in python pandas
eur3m.index = [datetime.datetime.strptime(x, '%d/%m/%Y') for x in eur3m.index]
