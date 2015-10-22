# Python pandas dataframe slicing, with if condition
df[df.categories.map(lambda cats: 'Restaurants' in cats)]
