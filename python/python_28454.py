# Dropping Columns in a Dataframe based on if they have a particular letter in the title
df_filtered = df[list(filter(lambda x: "F" not in x, df.columns))]
