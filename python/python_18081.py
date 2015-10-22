# Converting a column of strings to numbers in Pandas
actdf = pd.read_csv(StringIO(dataact), index_col=0, parse_dates=['date'], thousands=',')
