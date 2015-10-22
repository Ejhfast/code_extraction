# Python Tabs Uneven in Text File
with open('data.csv', 'a') as dataFile:
            csvWriter = csv.writer(dataFile, delimiter=',')
            csvWriter.writerow(productData)
