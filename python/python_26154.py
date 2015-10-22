# Python - count the number of words in text file that are also in csv word list
wanted = re.findall('\w+', open('CsvFileWithWords.csv').read().lower())
