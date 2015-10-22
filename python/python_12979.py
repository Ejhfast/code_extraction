# Issue in updating scraped data to the already existing csv using beautiful soup
with open('EE_AppendTesting.csv', 'a') as csvfile:
    spamwriter = csv.writer(csvfile, delimiter=',',lineterminator='\n')
