# Boxplot with pandas groupby
grouped = data['2013-08-17'].groupby(axis=1, level='SPECIES').T
grouped.boxplot()
