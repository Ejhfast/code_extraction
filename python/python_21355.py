# Pandas percentage of total with groupby
state_pcts = state_office.groupby(level=0).apply(lambda x: 100*x/float(x.sum()))
