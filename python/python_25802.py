# Pandas Python: Delete Rows of DF That Have ASCII Letters
df = df[~df['addzip'].str.contains("[a-zA-Z]").fillna(False)]
