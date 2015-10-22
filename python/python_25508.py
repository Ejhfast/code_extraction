# how do you read a pytables table into a pandas dataframe
a = tb.open_file("FGBS.h5")
table = a.root.quote.z4
c = pd.DataFrame.from_records(table.read())
