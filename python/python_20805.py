# Cannot interpolate on Pandas Dataframes
for col in df1.columns:
    df1[col] = df1[col].interpolate()
