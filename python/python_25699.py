# Filter groups based on occurrence of a value
df.groupby("Job").filter(lambda x : x["Dept"].isin(["TC"]).any())
