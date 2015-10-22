# Python Pandas: DataFrame filter negative values
for cols in data.columns.tolist()[1:]:
    data = data.ix[data[cols] &gt; 0]
