# How can I change the color of a grouped bar plot in Pandas?
df.groupby(['tags_0', 'gender']).gender.count().unstack().plot(kind='barh', legend=False, color=['r', 'g', 'b'])
