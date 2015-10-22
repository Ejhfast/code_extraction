# Conditional replacement in pandas
oldNewMap = {1: 3, 2: 3, 3: 4, 4: 2, 5: 1, 91: 6}
df['ethnicity'][df.year==year] = df['ethnicity'][df.year==year].map(oldNewMap)
