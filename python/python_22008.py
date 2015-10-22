# Concatenating data in different columns into a single column (pandas, python)
df["carpool_info"] =  df.apply(lambda x: "+".join([str(x[i]) for i in range(len(x))]),axis=1)
