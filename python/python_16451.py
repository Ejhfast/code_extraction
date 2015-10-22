# eliminate whitespaces in pd.read_csv
pd.read_csv('test.csv', sep='\s+#\s+', header=None).set_index(0)
