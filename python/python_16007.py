# print boolean True results of a regex match-Pandas Dataframe
print df[df.Resource.str.contains('pdf',na=False)][['IP', 'Time', 'Resource']][0:5]
