# Appending a Column with sum of rows and sorting in python
includingtotals = pd.concat([formatted,pd.DataFrame(formatted.sum(axis=1),columns=['Total'])],axis=1)
sorted = includingtotals.sort_index(by=['Total'], ascending=[False])
sorted.to_csv('byqualityissue.csv', header=True)
