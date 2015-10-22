# Sorting Pandas dataframe data within Groupby groups
tempDF.sort(['id','date']).groupby('id')['status'].last()
