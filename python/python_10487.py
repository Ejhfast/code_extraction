# How to group pandas DataFrame entries by date in a non-unique column
data.groupby(data['date'].map(lambda x: x.year))
