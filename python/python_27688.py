# How to create a data frame for each group in the pandas.groupby function?
d = {}
for name, group in data.groupby('hour'):
    d['group_' + str(name)] = group
