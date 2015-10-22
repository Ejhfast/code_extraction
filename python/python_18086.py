# How do you remove the column name row from a pandas DataFrame?
df.to_csv('filename.csv', sep=',' , header=False , index=False)
