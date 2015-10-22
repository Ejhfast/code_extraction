# Making OrderedDict out of Lists
graphdays = [pivot_table[(m)].astype(float).values for m in range(1, len(Days)+1)]
days_dict = OrderedDict(list(zip(Days, graphdays)))
