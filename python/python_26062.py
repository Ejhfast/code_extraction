# Deleting mulitple columns in Pandas
for col in df.columns:
    if 'Unnamed' in col:
        del df[col]
