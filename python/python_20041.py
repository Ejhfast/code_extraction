# Pandas Writing Dataframe Columns to csv
header = ["InviteTime (Oracle)", "Orig Number", "Orig IP Address", "Dest Number"]
df.to_csv('output.csv', columns = header)
