# How to get the max value of a multiple column group-by pandas?
annotations.ix[annotations.groupby(['bookid'], sort=False)['weight'].idxmax()][['bookid', 'conceptid', 'weight']]
