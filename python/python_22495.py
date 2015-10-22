# Pandas: How could I iterate two dataframes which have exactly same format?
for i in range(0, len(df_one.index)):
    for j in range(0, len(df_one.columns)):
        print df_one.values[i,j],df_two.value[i,j],i,j
