# Pandas dataframe with multiindex column - merge levels
grouped.columns = ['%s%s' % (a, '|%s' % b if b else '') for a, b in grouped.columns]
