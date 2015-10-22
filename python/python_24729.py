# Pandas framework: determining the count of a column data
counter = df["ItemID"].value_counts() #df is your dataframe
print counter[1] #prints how many times 1 occurred
