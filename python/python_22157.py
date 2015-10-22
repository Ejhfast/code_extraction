# Pandas Groupby Name of Day
df['day_name'] = df['pub_date'].apply(
    lambda x: pd.to_datetime(x).strftime("%A"))
