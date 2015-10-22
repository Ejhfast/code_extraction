# Pandas calculating age from a date
df1['age'] = now - datetime.strptime(df1['dob'], "%m%d%Y")
