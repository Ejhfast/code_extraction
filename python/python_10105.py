# Python mysqldb data
dicResults =  {}
for row in results:
    dicResults[row[1]] = [row[0], row[2], row[3]]
