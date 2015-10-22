# Constructing pandas dataframe with rows conditional on their not existing in another dataframe python
gcols = ['store', 'date']
tmp[tmp.set_index(gcols).index.isin(df.set_index(gcols).index) == False]
