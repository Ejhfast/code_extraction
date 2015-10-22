# Removing a row in a DataFrame when a or b or c is true
df = df[~df.Phase.isin(['xyz', 'ab', 'tlimit'])]
