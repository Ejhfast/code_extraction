# Python, Pandas : Return only those rows which have missing values
null_data = df[df.isnull().any(axis=1)]
