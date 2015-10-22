# Pandas convert dataframe to array of tuples
subset = data_set[['data_date', 'data_1', 'data_2']]
tuples = [tuple(x) for x in subset.values]
