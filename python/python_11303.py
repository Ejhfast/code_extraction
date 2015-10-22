# Typecasting before division (or any other mathematical operator) of columns in dataframes
df['C'] = df['A'] * 1.0 / df['B']
