# Pandas: How to access the value of the index
df["idx1_mod"] = df.index.get_level_values(0).values + 100
