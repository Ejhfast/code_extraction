# Pandas script modifying numbers to long float numbers when it shouldn't even be modifying that column/element
csvdata = pandas.read_csv('testing.csv', dtype={'TITLE5' : 'object', 'TITLE5.1' : 'object', 'TITLE5.2' : 'object', 'TITLE5.3' : 'object'})
