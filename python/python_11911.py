# Quickly applying string operations in a pandas DataFrame
splits = x['name'].split()
df['first'] = splits.str[0]
df['last'] = splits.str[1]
